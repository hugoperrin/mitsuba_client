"""File to define a cpu renderer."""
from typing import List, Union

import numpy as np
import torch
from loguru import logger

from mitsuba_client import default_gpu_mitsuba_variant
import mitsuba
mitsuba.set_variant(default_gpu_mitsuba_variant)

from mitsuba.render import Scene
from mitsuba_client.utils.return_types import ReturnType

from .cpu_renderer import CPURenderer


class GPURenderer(CPURenderer):
    """Renderer on gpu."""

    def __init__(self, mitsuba_variant: str = default_gpu_mitsuba_variant) -> None:
        logger.info(f"Loading GPU renderer with variant: {mitsuba_variant}")
        if "gpu" not in mitsuba_variant:
            raise ValueError(
                f"Variant: {mitsuba_variant} is not supported for gpu compute, please use the cpu renderer for this."
            )
        super().__init__(mitsuba_variant=mitsuba_variant)

    def render(
        self, scene: Scene, return_type: ReturnType = ReturnType.TORCH, **kwargs,
    ) -> List[Union[np.ndarray, torch.Tensor]]:
        """Render a given scene.

        Args:
            scene (Scene): The scene to render
            return_type (ReturnType, optional): The render type for the output.
                                Defaults to ReturnType.TENSOR.

        Returns:
            torch.Tensor: The output image.
        """
        results: List = super().render(
            scene=scene, return_type=return_type, **kwargs,
        )
        return results
