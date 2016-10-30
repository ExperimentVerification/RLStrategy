#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *
import random

class BoydEightyPercentNice(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self._lambda = Lambda(0.8) # initialised with 80% probability to cooperate

    def respond(self, game):
        # constant social coefficient of 0.8, being 80% nice throughout the entire IPD
        self._lambda.nochange()
        # NE for the lambda = 0.8
        return Strategy.NashEquilibrium(self._lambda)

    def name(self):
        return "Eighty Percent Nice from Boyd's Tournament"

    def author(self):
        return "Xiuyi Fan"