"""Utils for return types."""
from enum import Enum

import numpy as np
import torch

from mitsuba_client.utils.device import Device, GPUDevice, TypeDeviceEnum


def return_as_numpy(x: np.ndarray, **kwargs) -> np.ndarray:
    """Identity function for enum.

    Args:
        x (np.ndarray): Input array

    Returns:
        np.ndarray: Output array
    """
    return x


def return_as_torch(
    x: np.ndarray, device: Device = Device(type_device=TypeDeviceEnum.CPU), **kwargs,
) -> torch.Tensor:
    """Convert to torch on the right device.
        Glue is added for this simple task to rigidify the whole process.

    Args:
        x (np.ndarray): Input array
        device (Device): Device

    Returns:
        torch.Tensor: Output tensor
    """
    base_tensor: torch.Tensor = torch.from_numpy(x)
    if isinstance(device, GPUDevice):
        return base_tensor.cuda(device.num)
    return base_tensor


class ReturnType(Enum):
    NUMPY = return_as_numpy
    TORCH = return_as_torch
