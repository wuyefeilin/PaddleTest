#!/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf-8 vi:ts=4:sw=4:expandtab:ft=python
"""
test_functional_silu
"""

from apibase import APIBase
from apibase import sigmoid
from apibase import randtool
import paddle
import pytest
import numpy as np


class TestFunctionalSilu(APIBase):
    """
    test
    """

    def hook(self):
        """
        implement
        """
        self.types = [np.float32, np.float64]
        # self.debug = True
        # self.static = True
        # enable check grad
        # self.enable_backward = True


obj = TestFunctionalSilu(paddle.nn.functional.silu)


@pytest.mark.api_nn_Silu_vartype
def test_silu_base():
    """
    base
    """
    x = randtool("float", -10, 10, [3, 10, 3, 3])
    res = []
    for i in range(len(x.flatten())):
        tmp = x.flatten()[i] * sigmoid(x.flatten()[i])
        res.append(tmp)
    res = np.array(res).reshape(x.shape)
    # print(res)
    obj.base(res=res, x=x)


@pytest.mark.api_nn_Silu_parameters
def test_silu():
    """
    default
    """
    x = randtool("float", -1, 1, [4, 1, 3, 3])
    res = []
    for i in range(len(x.flatten())):
        tmp = x.flatten()[i] * sigmoid(x.flatten()[i])
        res.append(tmp)
    res = np.array(res).reshape(x.shape)
    # print(res)
    obj.run(res=res, x=x)