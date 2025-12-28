"""Robot configuration subpackage (vendored).

Upstream TacEx ships as an IsaacLab extension and auto-imports configuration
modules via `isaaclab_tasks.utils.import_packages`. Here we keep it best-effort
so `import tacex_assets` works even when `isaaclab_tasks` isn't installed.
"""

from __future__ import annotations

try:
    from isaaclab_tasks.utils import import_packages  # type: ignore

    _BLACKLIST_PKGS = ["utils"]
    import_packages(__name__, _BLACKLIST_PKGS)
except Exception:
    # Users can still import configs explicitly, e.g.:
    #   from tacex_assets.robots.franka.franka_gsmini_gripper_rigid import ...
    pass
