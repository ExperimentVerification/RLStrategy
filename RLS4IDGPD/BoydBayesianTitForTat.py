#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *
import random
# not suitable for RL-based parameter updating
class BoydBayesianTitForTat(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self._lambda = Lambda(random.gauss(0.0,1.0) + 0.3) # only know the distribution of the parameter

    def respond(self, game):
        if self.getRoundsPlayed() == 0:
            self._lambda.nochange()
        else:
            MyLast = self.getLastResponsePair()[0]
            OppLast = self.getLastResponsePair()[1]
            # parameter adjusting
            if MyLast == 'C' and OppLast == 'C':
                self._lambda.nochange()
            elif (MyLast == 'C' and OppLast == 'D') or (MyLast == 'D' and OppLast == 'C'):
                if random.gauss(0.0, 1.0) < self._lambda.getValue():
                    self._lambda.decrementValue()
                else:
                    self._lambda.incrementValue()
            elif MyLast == 'D' and OppLast == 'D':
                self._lambda.incrementValue()

        # use NE for the updated social coefficient for decision making
        return Strategy.NashEquilibrium(self._lambda)

    def name(self):
        return "Bayesian Tit For Tat from Boyd's Tournament"

    def author(self):
        return "Ingrid Funie"