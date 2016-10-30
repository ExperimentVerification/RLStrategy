#!/usr/bin/env python
# -*- coding: utf-8 -*-

# random shift for the action that has been chossen
# 25% from D to C
# 25% from C to D
from Strategy import *
from Lambda import *
import random

class BoydABitRandom(Strategy):

    def __init__(self, game):
        Strategy.__init__(self)
        self._lambda = Lambda(0.1)

    def respond(self, game):
        if self.getRoundsPlayed() == 0:
            self._lambda.nochange()
        else:
            MyLast = self.getLastResponsePair()[0]
            OppLast = self.getLastResponsePair()[1]
            # adjust the lambda according to the AEGSS
            if MyLast == 'C' and OppLast == 'C':
                self._lambda.nochange()
            elif MyLast == 'C' and OppLast == 'D':
                self._lambda.incrementValue()
            elif MyLast == 'D' and OppLast == 'C':
                self._lambda.decrementValue()
            elif MyLast == 'D' and OppLast == 'D':
                self._lambda.incrementValue()

        resp = Strategy.NashEquilibrium(self._lambda)

        if resp == 'D':
            if random.randint(1, 19) < 5:
                resp = 'C'
        elif resp == 'C':
            if random.randint(1, 19) < 5:
                resp = 'D'

        return resp

    def name(self):
        return "A Bit Random from Boyd's Tournament"

    def author(self):
        return "Xiuyi Fan"