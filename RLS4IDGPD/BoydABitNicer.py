#!/usr/bin/env python
# -*- coding: utf-8 -*-

# can be applied to general double game
# RL-based parameter updating is not suitable for this strategy,
# because the main idea of it is to adjust the social coefficient
from Strategy import *
from Lambda import *

class BoydABitNicer(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self._lambda = Lambda(0.1)
        self.myCtr = 0 # counting my cooperation times
        self.oppCtr = 0 # counting the opponent's cooperation times

    def respond(self, game):
        if self.getRoundsPlayed() == 0:
            self._lambda.nochange()
        else:
            MyLast = self.getLastResponsePair()[0]
            OppLast = self.getLastResponsePair()[1]

            if MyLast == 'C':
                self.myCtr += 1
            if OppLast == 'C':
                self.oppCtr += 1
            # adjust the lambda according to the difference of cooperation times
            if self.myCtr < self.oppCtr + 10:
                self._lambda.incrementValue()
            elif self.myCtr > self.oppCtr + 20:
                self._lambda.decrementValue()
            else:
                self._lambda.nochange()

        return Strategy.NashEquilibrium(self._lambda)

    def name(self):
        return "A Bit Nicer from Boyd's Tournament"

    def author(self):
        return "Xiuyi Fan"