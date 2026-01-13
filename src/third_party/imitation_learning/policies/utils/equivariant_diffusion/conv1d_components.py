import torch
import torch.nn as nn
import torch.nn.functional as F

from ...vision.vec_layers import VecActivation


class VecDownsample1d(nn.Module):
    def __init__(self, in_dim, out_dim=None, kernel_size=3, stride=2, padding=1):
        super().__init__()
        if out_dim is None:
            out_dim = in_dim
        self.conv = nn.Conv1d(in_dim, out_dim, kernel_size, stride, padding, bias=False)

    def forward(self, x):

        original_shape = x.shape
        x_flattened = torch.transpose(x, 1, 2)
        x_flattened = x_flattened.reshape(-1, *x_flattened.shape[2:])
        out = self.conv(x_flattened)

        out = torch.transpose(out.reshape(-1, 3, *out.shape[1:]), 1, 2)
        return out


class VecUpsample1d(VecDownsample1d):
    def __init__(self, dim):
        nn.Module.__init__(self)
        self.conv = nn.ConvTranspose1d(dim, dim, 4, 2, 1, bias=False)


class VecConv1dBlock(nn.Module):
    def __init__(self, inp_channels, out_channels, kernel_size):

        super().__init__()

        self.block = nn.Sequential(
            VecDownsample1d(
                inp_channels, out_channels, kernel_size, 1, kernel_size // 2
            ),
            VecActivation(
                out_channels,
                nn.Mish(),
                shared_nonlinearity=False,
                mode="so3",
                cross=False,
            ),
        )

    def forward(self, x):
        return self.block(x)


def test():
    cb = VecConv1dBlock(256, 128, kernel_size=3)
    x = torch.zeros((1, 256, 3, 16))
    o = cb(x)
