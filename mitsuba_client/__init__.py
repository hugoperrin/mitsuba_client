"""Module for the cli usage."""
import os

import mitsuba

default_mitsuba_variant: str = os.getenv("MITSUBA_VARIANT", "packet_rgb")
default_gpu_mitsuba_variant: str = "gpu"

mitsuba.set_variant(default_mitsuba_variant)
