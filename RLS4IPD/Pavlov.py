#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pavlov: Cooperates on the first move. If a reward(CC in the round before the last round) or
# a temptation(DC in the round before the last round)
# payoff is received in the last round the repeat last choice, otherwise choose the opposite choice.
# also called win-stay-lose-shift - cooperates on the first move and defects only if
# both the players did not agree on the previous move
from Strategy import *

class Pavlov(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        # self.beforeLast = []

    def respond(self, game):
        if self.getLastResponsePair() == 0:
            # C on the first move
            return 'C'
        else:
            if self.getLastResponsePair()[0]  == self.getLastResponsePair()[1]:
                return 'C'
            else:
                return 'D'

    def name(self):
        return "Pavlov"

    def author(self):
        return "******"