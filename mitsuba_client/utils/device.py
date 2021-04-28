"""File to handle well devices."""
from dataclasses import dataclass
from enum import Enum


class TypeDeviceEnum(Enum):
    """Enum for device type."""

    GPU = "cuda"
    CPU = "cpu"

    @staticmethod
    def build_safe_from_str(str_value: str):
        """Build the enum safely.

        Args:
            str_value (str): Input string

        Returns:
            [TypeDeviceEnum]: The enum value
                    it defaults to cpu if string unrecognized
        """
        if str_value in ["gpu", "cuda"]:
            return TypeDeviceEnum.GPU
        else:
            return TypeDeviceEnum.CPU


@dataclass
class Device:
    """Base dataclass for device."""

    type_device: TypeDeviceEnum


@dataclass
class GPUDevice(Device):
    """Dataclass for gpu device."""

    num: int = 0
