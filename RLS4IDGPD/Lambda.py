#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BaseLambda import *
# social coefficient from 0.0 to 1.0, the unit for changing is 0.2
class Lambda(BaseLambda):
    def __init__(self, startValue):
        BaseLambda.__init__(self, 0.0, 1.0, 0.2, startValue)