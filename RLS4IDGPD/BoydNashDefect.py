#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *
# RL-version see RLAEGS
# like the ALLD for the IPD
class BoydNashDefect(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self._lambda = Lambda(0.0) # only play the material game

    def respond(self, game):
        self._lambda.nochange() # constant value
        return Strategy.NashEquilibrium(self._lambda) # D

    def name(self):
        return "Nash Defects from Boyd's Tournament"

    def author(self):
        return "Xin Yan"