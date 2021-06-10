"""File to define a cpu renderer."""
import os
from typing import List, Optional, Union

import numpy as np
import pyexr
import torch
from loguru import logger
from tqdm import tqdm

from mitsuba_client import default_gpu_mitsuba_variant
import mitsuba
mitsuba.set_variant(default_gpu_mitsuba_variant)

from mitsuba.render import Scene
from mitsuba_client.utils.return_types import ReturnType

from .gpu_renderer import GPURenderer


class MultiplePassGPURenderer(GPURenderer):
    """Renderer on gpu with multiple passees => averaging results in order to avoid OOM VRAM errors."""

    def __init__(
        self,
        mitsuba_variant: str = default_gpu_mitsuba_variant,
        progressive_render_folder_path: Optional[str] = None,
    ) -> None:
        """ MultiplePassGPURenderer

        Args:
            mitsuba_variant (str, optional): The mitsuba variant to use. Defaults to default_gpu_mitsuba_variant.
            progressive_render_folder_path (Optional[str], optional): The folder path to use if writing intermediary results. Defaults to None.
        """
        self.progressive_render_folder_path: Optional[
            str
        ] = progressive_render_folder_path
        if self.progressive_render_folder_path is not None:
            os.makedirs(os.path.abspath(self.progressive_render_folder_path))
        super().__init__(mitsuba_variant=mitsuba_variant)

    def render(
        self,
        scene: Scene,
        return_type: ReturnType = ReturnType.TORCH,
        n_pass: int = 1,
        **kwargs,
    ) -> List[Union[np.ndarray, torch.Tensor]]:
        """Render a given scene.

        Args:
            scene (Scene): The scene to render
            return_type (ReturnType, optional): The render type for the output.
                                Defaults to ReturnType.TENSOR.

        Returns:
            torch.Tensor: The output image.
        """
        results: Optional[List] = None
        for k in tqdm(range(n_pass)):
            results_tmp: List = super().render(
                scene=scene, return_type=return_type, **kwargs,
            )
            logger.debug(f"At iter: {k}: {np.mean(results_tmp[0])}")
            if results is None:
                results = results_tmp
                continue
            for i, _ in enumerate(results):
                results[i] += results_tmp[i]
                if self.progressive_render_folder_path is not None:
                    pyexr.write(
                        os.path.join(
                            self.progressive_render_folder_path, f"render_{k}_{i}.exr"
                        ),
                        data=results_tmp[i],
                    )
        for i, _ in enumerate(results):
            results[i] /= n_pass
        return results
