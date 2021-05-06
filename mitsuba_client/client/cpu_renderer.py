"""File to define a gpu renderer."""


from typing import List, Union

import numpy as np
import torch

from mitsuba.core import Bitmap, Struct
from mitsuba.render import Scene
from mitsuba_client import default_mitsuba_variant
from mitsuba_client.utils.return_types import ReturnType

from .renderer import Renderer


class CPURenderer(Renderer):
    """Renderer on cpu."""

    def __init__(self, mitsuba_variant: str = default_mitsuba_variant) -> None:
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
        results: List = []
        for sensor in scene.sensors():
            scene.integrator().render(scene, sensor)
            film = sensor.film()
            img = film.bitmap(raw=True).convert(
                Bitmap.PixelFormat.RGB, Struct.Type.Float32, srgb_gamma=True,
            )
            results.append(np.array(img))
        return results
