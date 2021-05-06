"""File to define a cpu renderer."""
from mitsuba_client import default_gpu_mitsuba_variant

from .cpu_renderer import CPURenderer


class GPURenderer(CPURenderer):
    """Renderer on gpu."""

    def __init__(self, mitsuba_variant: str = default_gpu_mitsuba_variant) -> None:
        if "gpu" not in mitsuba_variant:
            raise ValueError(
                f"Variant: {mitsuba_variant} is not supported for gpu compute, please use the cpu renderer for this."
            )
        super().__init__(mitsuba_variant=mitsuba_variant)
