#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *
import random
# not suitable for RL-based parameter updating
class BoydBayesian(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        # use a Gaussian (mean 0) + 0.5 to offset it
        self._lambda = Lambda(random.gauss(0.0,1.0) + 0.5)

    def respond(self, game):
        if self.getRoundsPlayed() == 0:
            self._lambda.nochange()
        else:
            # random parameter adjusting
            if random.gauss(0.0, 1.0) + 0.5 < self._lambda.getValue():
                self._lambda.decrementValue()
            elif random.gauss(0.0, 1.0) + 0.5 > self._lambda.getValue():
                self._lambda.incrementValue()

        return Strategy.NashEquilibrium(self._lambda)

    def name(self):
        return "Bayesian from Boyd's Tournament"

    def author(self):
        return "In-house (Ali Ghoroghi)"