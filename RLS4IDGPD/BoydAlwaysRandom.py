#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *
import random

class BoydAlwaysRandom(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self._lambda = Lambda(random.random()) # random initial lambda

    def respond(self, game):
        self._lambda.nochange()
        # random action with even chance
        if random.random() < 0.5:
            return 'C'
        else:
            return 'D'

    def name(self):
        return "Always Random from Boyd's Tournament"

    def author(self):
        return "In-house (Theodore Boyd)"