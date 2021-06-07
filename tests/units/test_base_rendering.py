"""Test base rendering on cpu."""
import os
import unittest
from typing import List

import numpy as np

import mitsuba
from mitsuba_client.client.rendering_env import RendererEnv

mitsuba.set_variant("packet_rgb")



class TestBaseRendering(unittest.TestCase):
    def test_rendering_cpu(self):
        path_scene: str = os.path.join("scenes", "bathroom", "scene.xml")
        env: RendererEnv = RendererEnv()
        env.load_scene(scene_path=path_scene, scene_id="test")
        imgs: List = env.render("test")
        self.assertIsInstance(imgs, list)
        for img in imgs:
            self.assertIsInstance(img, np.ndarray)
            self.assertTrue(img.shape == (2560, 1440, 3))
