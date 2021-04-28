"""Tests for device classes."""
import unittest

from mitsuba_client.utils.device import Device, GPUDevice, TypeDeviceEnum


class TestDevices(unittest.TestCase):
    def test_device_inits(self):
        cpu_dev: Device = Device(type_device=TypeDeviceEnum.CPU)
        gpu_dev: Device = GPUDevice(type_device=TypeDeviceEnum.GPU)

        self.assertEqual(gpu_dev.num, 0)
        self.assertEqual(cpu_dev.type_device, TypeDeviceEnum.CPU)
