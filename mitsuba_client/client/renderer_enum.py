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
