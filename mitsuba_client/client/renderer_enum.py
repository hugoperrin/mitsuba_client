"""Renderer enum to get the right renderer with a way to get only accessible renderers."""
from enum import Enum

from .cpu_renderer import CPURenderer
from .gpu_renderer import GPURenderer
from .multipass_gpu_renderer import MultiplePassGPURenderer


class RendererEnum(Enum):
    CPU = CPURenderer
    GPU = GPURenderer
    GPU_MULTIPASS = MultiplePassGPURenderer
    ADAPTIVE_SAMPLING = None

    @staticmethod
    def from_str(str_value: str):
        if str_value == "cpu":
            return RendererEnum.CPU
        elif str_value == "gpu":
            return RendererEnum.GPU
        elif str_value == "gpu_multi":
            return RendererEnum.GPU_MULTIPASS
        elif str_value == "adaptive_gpu":
            return RendererEnum.ADAPTIVE_SAMPLING
        else:
            raise ValueError(f"Value: ({str_value}) is not a valid renderer string")

    def default_variant(self):
        if self == RendererEnum.CPU:
            return "packet_rgb"
        else:
            return "gpu_rgb"
