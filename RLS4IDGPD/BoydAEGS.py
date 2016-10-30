#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *
from Lambda import *
import random

class BoydAEGS(Strategy):

    def __init__(self, game):
        Strategy.__init__(self)
        self._lambda = Lambda(0.0)

    def respond(self, game):
        if self.getRoundsPlayed() == 0:
            self._lambda.nochange()
        else:
            MyLast = self.getLastResponsePair()[0]
            OppLast = self.getLastResponsePair()[1]
            if MyLast == 'C' and OppLast == 'C':
                self._lambda.incrementValue()
            elif MyLast == 'C' and OppLast == 'D':
                self._lambda.incrementValue()
            elif MyLast == 'D' and OppLast == 'C':
                self._lambda.decrementValue()
            elif MyLast == 'D' and OppLast == 'D':
                self._lambda.incrementValue()

        return Strategy.NashEquilibrium(self._lambda)

    def name(self):
        return "AE-GS from Boyd's Tournament"

    def author(self):
        return "In-house (Georgios Sakellariou)"