#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tit for Two Tats(TFTT): Cooperates on the first two moves, then defects only if the opponent has defected
# during the two previous moves
from Strategy import *

class TFTT(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self.lastTwoOpp = []

    def respond(self, game):
        if self.getLastResponsePair() == 0:
            return 'C'
        else:
            self.lastTwoOpp.append(self.getLastResponsePair()[1])
            if len(self.lastTwoOpp) < 2:
                return 'C'
            else:
                tmp = self.lastTwoOpp[0]
                self.lastTwoOpp.pop(0)

                if self.lastTwoOpp[0] =='D' and tmp == 'D':
                    return 'D'

                return 'C'

    def name(self):
        return "Tit for Two Tats"

    def author(self):
        return "******"