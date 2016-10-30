#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *
# do not increase the value of the social coefficient, so negative
class BoydNegativePeople(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self._lambda = Lambda(random.random())

    def respond(self, game):
        if self.getRoundsPlayed() == 0:
            self._lambda.nochange()
        else:
            if self.getLastResponsePair()[1] == 'D':
                # response to the opponent's defection
                self._lambda.decrementValue()
            else:
                self._lambda.nochange()
        return Strategy.NashEquilibrium(self._lambda)

    def name(self):
        return "Negative People from Boyd's Tournament"

    def author(self):
        return "In-house (Ali Ghoroghi)"