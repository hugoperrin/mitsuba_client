"""Module for the cli usage."""
import os


default_mitsuba_variant: str = os.getenv("MITSUBA_VARIANT", "packet_rgb")
default_gpu_mitsuba_variant: str = "gpu_rgb"
