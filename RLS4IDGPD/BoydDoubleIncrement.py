#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *
import random
# Similar to the AEGSS, in which the increment of the parameter always takes twice
class BoydDoubleIncrement(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        # use a Gaussian (mean 0) + 0.5 to offset it
        self._lambda = Lambda(0.1)

    def respond(self, game):
        if self.getRoundsPlayed() == 0:
            self._lambda.nochange()
        else:
            MyLast = self.getLastResponsePair()[0]
            OppLast = self.getLastResponsePair()[1]
            if MyLast == 'C' and OppLast == 'C':
                self._lambda.nochange()
            elif MyLast == 'C' and OppLast == 'D':
                # double increase
                self._lambda.incrementValue()
                self._lambda.incrementValue()
            elif MyLast == 'D' and OppLast == 'C':
                self._lambda.decrementValue()
            elif MyLast == 'D' and OppLast == 'D':
                # double increase
                self._lambda.incrementValue()
                self._lambda.incrementValue()

        return Strategy.NashEquilibrium(self._lambda)

    def name(self):
        return "Double Increment from Boyd's Tournament"

    def author(self):
        return "Xiuyi Fan"