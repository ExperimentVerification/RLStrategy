#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *
import random

class BoydRandomTitForTat(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self._lambda = Lambda(random.random())

    def respond(self, game):
        # play C and D with even chance
        # use a constant random social coefficient
        if random.randint(0,9) % 2 == 0:
            self._lambda.nochange()
            return 'D'
        else:
            self._lambda.nochange()
            return 'C'

    def name(self):
        return "Random Tit For Tat from Boyd's Tournament"

    def author(self):
        return "Aga Madurska"