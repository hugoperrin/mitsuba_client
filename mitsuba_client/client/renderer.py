"""Class for renderer of a single scene at once."""
from typing import Union

import numpy as np
import torch
from loguru import logger

import mitsuba
from mitsuba.render import Scene
from mitsuba_client import default_mitsuba_variant
from mitsuba_client.utils.return_types import ReturnType


class Renderer:
    """Abstract class for the renderer wrapper."""

    def __init__(self, mitsuba_variant: str = default_mitsuba_variant) -> None:
        logger.info(f"Loading renderer with variant: {mitsuba_variant}")
        mitsuba.set_variant(mitsuba_variant)
        self.mitsuba_variant: str = mitsuba_variant

    def render(
        self, scene: Scene, return_type: ReturnType = ReturnType.NUMPY, **kwargs,
    ) -> Union[torch.Tensor, np.ndarray]:
        """Render a given scene.

        Args:
            scene (Scene): The scene to render
            return_type (ReturnType, optional): The render type for the output.
                                Defaults to ReturnType.NUMPY.

        Returns:
            Union[torch.Tensor, np.ndarray]: The output image.
        """
        raise NotImplementedError
