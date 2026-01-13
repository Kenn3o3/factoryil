import torch

EPS = 1e-8

def _skew(v):
    # v: (...,3)
    O = torch.zeros_like(v[..., 0])
    vx, vy, vz = v[..., 0], v[..., 1], v[..., 2]
    return torch.stack(
        [
            torch.stack([O, -vz, vy], dim=-1),
            torch.stack([vz, O, -vx], dim=-1),
            torch.stack([-vy, vx, O], dim=-1),
        ],
        dim=-2,
    )

def so3_exp_map(omega):
    """
    Axis-angle to rotation matrix. omega: (..., 3)
    Returns: (..., 3, 3)
    """
    theta = torch.linalg.norm(omega, dim=-1, keepdim=True).clamp(min=EPS)  # (...,1)
    k = omega / theta  # (...,3)
    K = _skew(k)       # (...,3,3)
    I = torch.eye(3, device=omega.device, dtype=omega.dtype).expand(*omega.shape[:-1], 3, 3)
    s = torch.sin(theta)[..., None]  # (...,1,1)
    c = torch.cos(theta)[..., None]
    R = I + s * K + (1 - c) * (K @ K)
    # Handle small-angle numerics by Taylor expansion near 0
    small = (theta.squeeze(-1) < 1e-6)[..., None, None]
    if small.any():
        # Use 1st order: R ≈ I + [omega]_x
        K_omega = _skew(omega)
        R_small = I + K_omega
        R = torch.where(small, R_small, R)
    return R

def so3_log_map(R):
    """
    Rotation matrix to axis-angle. R: (...,3,3)
    Returns: (...,3) axis-angle vector
    """
    # Clamp trace to [-1,3]
    tr = (R[..., 0, 0] + R[..., 1, 1] + R[..., 2, 2]).clamp(-1.0, 3.0)
    cos_theta = (tr - 1.0) / 2.0
    cos_theta = cos_theta.clamp(-1.0, 1.0)
    theta = torch.acos(cos_theta)  # (...,)

    # For general case
    wx = R[..., 2, 1] - R[..., 1, 2]
    wy = R[..., 0, 2] - R[..., 2, 0]
    wz = R[..., 1, 0] - R[..., 0, 1]
    w = torch.stack([wx, wy, wz], dim=-1)  # (...,3)

    # Avoid division by zero
    denom = 2.0 * torch.sin(theta).unsqueeze(-1).clamp(min=EPS)
    v = theta.unsqueeze(-1) * (w / denom)

    # Near zero angle: use first-order approx v ≈ vee(R - R^T)/2
    small = (theta.abs() < 1e-6)[..., None]
    v_small = 0.5 * torch.stack(
        [R[..., 2, 1] - R[..., 1, 2],
         R[..., 0, 2] - R[..., 2, 0],
         R[..., 1, 0] - R[..., 0, 1]], dim=-1
    )
    v = torch.where(small, v_small, v)
    return v

def compose_axis_angles(a, b):
    """
    Compose rotations Exp(a) * Exp(b) = Exp(c), return c.
    a, b: (...,3)
    """
    Ra = so3_exp_map(a)
    Rb = so3_exp_map(b)
    Rc = Ra @ Rb
    return so3_log_map(Rc)

def relative_axis_angle(a_from, a_to):
    """
    Compute relative rotation r s.t. Exp(a_from)^T Exp(a_to) = Exp(r).
    """
    Rf = so3_exp_map(a_from)
    Rt = so3_exp_map(a_to)
    Rrel = Rf.transpose(-1, -2) @ Rt
    return so3_log_map(Rrel)

def vec6d_to_R(eef_pos_6drot):
    """
    Convert 6D rotation representation stored in state (two columns of R) to orthonormal R.
    eef_pos_6drot: (..., 6) with first 3 pos, next two 3D vectors as R[:,0], R[:,1].
    Returns: (..., 3, 3)
    """
    x = eef_pos_6drot[..., 0:3]  # not used here (pos)
    c1 = eef_pos_6drot[..., 3:6]
    c2 = eef_pos_6drot[..., 6:9] if eef_pos_6drot.shape[-1] >= 9 else None
    if c2 is None:
        # Fallback: identity
        I = torch.eye(3, device=eef_pos_6drot.device, dtype=eef_pos_6drot.dtype)
        tgt = I.expand(*eef_pos_6drot.shape[:-1], 3, 3)
        return tgt
    u1 = torch.nn.functional.normalize(c1, dim=-1)
    u2 = c2 - (u1 * c2).sum(-1, keepdim=True) * u1
    u2 = torch.nn.functional.normalize(u2, dim=-1)
    u3 = torch.cross(u1, u2, dim=-1)
    R = torch.stack([u1, u2, u3], dim=-1)  # (...,3,3), columns
    return R