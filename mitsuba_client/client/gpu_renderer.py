"""File to define a gpu renderer."""


import torch

from mitsuba.render import Scene
from mitsuba_client import default_gpu_mitsuba_variant
from mitsuba_client.utils.return_types import ReturnType

from .renderer import Renderer


class GPURenderer(Renderer):
    """Renderer on gpu."""

    def __init__(self, mitsuba_variant: str = default_gpu_mitsuba_variant) -> None:
        if "gpu" not in mitsuba_variant:
            raise ValueError(
                f"Variant: {mitsuba_variant} is not supported for gpu compute, please use the cpu renderer for this."
            )
        super().__init__(mitsuba_variant=mitsuba_variant)

    def render(
        self, scene: Scene, return_type: ReturnType = ReturnType.TORCH, **kwargs,
    ) -> torch.Tensor:
        """Render a given scene.

        Args:
            scene (Scene): The scene to render
            return_type (ReturnType, optional): The render type for the output.
                                Defaults to ReturnType.TENSOR.

        Returns:
            torch.Tensor: The output image.
        """

        # TODO: do the rendering on gpu loop
        raise NotImplementedError
