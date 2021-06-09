"""Test base rendering on cpu."""
import os
import unittest
from typing import List

import numpy as np
from loguru import logger

import mitsuba
from mitsuba_client.client.renderer_enum import RendererEnum
from mitsuba_client.client.rendering_env import RendererEnv

mitsuba.set_variant("gpu_rgb")


class TestBaseRendering(unittest.TestCase):
    def test_rendering_gpu(self):
        path_scene: str = os.path.join("scenes", "bathroom", "scene.xml")
        env: RendererEnv = RendererEnv(
            mitsuba_variant="gpu_rgb", renderer_type=RendererEnum.GPU
        )
        env.load_scene(scene_path=path_scene, scene_id="test")
        imgs: List = env.render("test")
        self.assertIsInstance(imgs, list)
        for img in imgs:
            logger.warning(f"Shape is: {img.shape}")
            self.assertIsInstance(img, np.ndarray)
            self.assertTrue(img.shape == (1440, 2560, 3))
