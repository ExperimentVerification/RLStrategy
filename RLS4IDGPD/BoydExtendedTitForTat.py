#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *
import random
# not suitable for RL-based parameter updating
class BoydExtendedTitForTat(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self._lambda = Lambda(0.5)

    def respond(self, game):
        if self.getRoundsPlayed() == 0 or self.getRoundsPlayed() == 1:
            # for the first two rounds, do not change lambda and cooperate
            self._lambda.nochange()
            return 'C'
        elif self.getRoundsPlayed() % 10 < 4:
            # from the third round, for the rounds ending 3, 0, 1, 2: increase the social coefficient by one unit and C
            self._lambda.incrementValue()
            return 'C'
        elif self.getRoundsPlayed() % 2 == 0:
            # for the rounds ending 4, 6, 8: decrease lambda and defect
            self._lambda.decrementValue()
            return 'D'
        else:
            # for the rest of the moves, adjust the lambda according to the opponent's last action
            if self.getLastResponsePair()[1] == 'C':
                self._lambda.incrementValue()
            else:
                self._lambda.decrementValue()
            # use NE for the updated parametern for decision making
            return Strategy.NashEquilibrium(self._lambda)

    def name(self):
        return "Extended Tit For Tat from Boyd's Tournament"

    def author(self):
        return "In-house (Theodore Boyd)"