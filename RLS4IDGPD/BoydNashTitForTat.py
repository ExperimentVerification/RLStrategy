#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *

class BoydNashTitForTat(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self._lambda = Lambda(random.random()) # random initialisation

    def respond(self, game):
        if self.getRoundsPlayed() == 0:
            # first round
            self._lambda.nochange()
            return 'C'
        else:
            # from the second round, adjust the parameter according the opponent's last action
            if self.getLastResponsePair()[1] == 'C':
                # C for lambda increase, meaning higher probability to cooperate
                self._lambda.incrementValue()
            else:
                self._lambda.decrementValue()
            # always use the NE for the updated social coefficient
            return Strategy.NashEquilibrium(self._lambda)

    def name(self):
        return "Nash Tit For Tat from Boyd's Tournament"

    def author(self):
        return "In-house (Ali Ghoroghi)"