#!/usr/bin/env python
# -*- coding: utf-8 -*-

# hard_tft, cooperates on the first two moves, then defects only if the opponent has defected one of the previous two moves
from Strategy import *

class hard_tft(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self.OppLast2 = []

    def respond(self, game):
        if self.getLastResponsePair() == 0:
            return 'C'
        else:
            self.OppLast2.append(self.getLastResponsePair()[1])
            if len(self.OppLast2) < 2:
                return 'C'
            else:
                a = self.OppLast2[0]
                b = self.OppLast2[1]
                self.OppLast2.pop(0)

                if a == 'D' or b == 'D':
                    return 'D'

                return 'C'

    def name(self):
        return "Hard Tit for Tat - last two"

    def author(self):
        return "******"