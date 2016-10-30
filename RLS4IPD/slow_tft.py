#!/usr/bin/env python
# -*- coding: utf-8 -*-

# slow_tft, cooperates the two first moves, then begin to defect after two consecutive defections of its
# opponent; returns to cooperation after two consecutive cooperations of its opponent.
from Strategy import *

class slow_tft(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self.OppLast2 = []
        self.currentA = ''
        # self.defect = False

    def respond(self, game):
        if self.getLastResponsePair() == 0:
            return 'C'
        else:
            self.OppLast2.append(self.getLastResponsePair()[1])

            if len(self.OppLast2) < 2:
                # C on the second move
                return 'C'
            else:
                tmp = self.OppLast2[0]
                self.OppLast2.pop(0)

                if self.OppLast2[0] == tmp:
                    self.currentA = tmp
                    return tmp

                return self.currentA


    def name(self):
        return "Slow Tit For Tat"

    def author(self):
        return "******"