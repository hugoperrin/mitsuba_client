"""Tests for device classes."""
import unittest

import numpy as np
import torch

from mitsuba_client.utils.return_types import ReturnType


class TestReturntype(unittest.TestCase):
    def test_return_type_numpy(self):
        ret_type: ReturnType = ReturnType.NUMPY
        a = np.ones(10)
        res = ret_type(a)

        self.assertIsInstance(res, np.ndarray)
        self.assertTrue((res == a).all())

    def test_return_type_torch(self):
        ret_type: ReturnType = ReturnType.TORCH
        a = np.ones(10)
        res = ret_type(a)

        self.assertIsInstance(res, torch.Tensor)
        self.assertTrue((res.numpy() == a).all())
