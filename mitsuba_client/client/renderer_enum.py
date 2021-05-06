"""Renderer enum to get the right renderer with a way to get only accessible renderers."""
from enum import Enum

from .cpu_renderer import CPURenderer
from .gpu_renderer import GPURenderer


class RendererEnum(Enum):
    CPU = CPURenderer
    GPU = GPURenderer
    ADAPTIVE_SAMPLING = None
