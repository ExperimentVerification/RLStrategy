#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Prober: Start with D, C, C and then defect if the opponent has cooperated in the second and third move;
# otherwise, play TFT

from Strategy import *

class Prober(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self.OppSecThi = []
        self.DFlag = False

    def respond(self, game):
        if self.getLastResponsePair() == 0:
            # D
            return 'D'
        else:
            if len(self.OppSecThi) < 2:
                # CC
                self.OppSecThi.append(self.getLastResponsePair()[1])
                return 'C'
            else:
                if len(self.OppSecThi) == 2:
                    self.OppSecThi.pop(0)
                    self.OppSecThi.append(self.getLastResponsePair()[1])
                    if self.OppSecThi[0] == 'C' and self.OppSecThi[1] == 'C':
                        self.DFlag = True
                    self.OppSecThi.append('END')

                if self.DFlag:
                    return 'D'
                else:
                    return self.getLastResponsePair()[1]

    def name(self):
        return "Prober"

    def author(self):
        return "******"