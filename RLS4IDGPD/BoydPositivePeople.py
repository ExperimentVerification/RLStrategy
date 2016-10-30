#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *

class BoydPositivePeople(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self._lambda = Lambda(random.random())

    def respond(self, game):
        if self.getRoundsPlayed() == 0:
            self._lambda.nochange()
        else:
            if self.getLastResponsePair()[1] == 'C':
                # only has positive response to the opponent's cooperation
                self._lambda.incrementValue()
            else:
                self._lambda.nochange()
        return Strategy.NashEquilibrium(self._lambda)

    def name(self):
        return "Positive People from Boyd's Tournament"

    def author(self):
        return "In-house (Ali Ghoroghi)"