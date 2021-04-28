"""Class for rendering environment: i.e multiple scenes."""
from typing import Dict, Optional

import mitsuba
from mitsuba.core.xml import load_file
from mitsuba.render import Scene
from mitsuba_client import default_mitsuba_variant

from .renderer import Renderer


class RendererEnv:
    """Class for the renderer wrapper."""

    def __init__(self, mitsuba_variant: str = default_mitsuba_variant) -> None:
        """Init environement for rendering."""
        mitsuba.set_variant(mitsuba_variant)
        self.renderer = Renderer()
        self.scenes: Dict[str, Scene] = {}

    def load_scene(self, scene_path: str, scene_id: Optional[str] = None):
        """Load a scene from its path.

        Args:
            scene_path (str): The scene path
        """
        if scene_id is None:
            scene_id = scene_path
        scene: Scene = load_file(scene_path)
        self.scenes[scene_id] = scene

    def render(self, scene_id: str, **kwargs):
        """Render a given scene."""
        scene = self.get_scene_from_id(scene_id)
        self.renderer.render(scene=scene)

    def get_scene_from_id(self, scene_id: str, **kwargs):
        """Get scene from its string id.

        Args:
            scene_id (str): The id of the scene
        """
        try:
            return self.scenes[scene_id]
        except KeyError:
            raise ValueError(
                f"Scene with id: {scene_id} does not exist in scene list with keys: {self.scenes.keys()}",
            )
