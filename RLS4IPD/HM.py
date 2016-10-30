#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Hard Majority(HM): Defects on the first move, and defects if the number of defections of the opponent is
# greater than or equal to the number of times it has cooperated, else cooperates.
from Strategy import *

class HM(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self.OppC = 0
        self.OppD = 0

    def respond(self, game):
        if self.getLastResponsePair() == 0:
            return 'D'
        else:
            # count for the cooperation and defection times
            if self.getLastResponsePair()[1] == 'D':
                self.OppD += 1
            else:
                self.OppC += 1

            # make decision according to the defection and cooperation times
            if self.OppD >= self.OppC:
                return 'D'
            else:
                return 'C'


    def name(self):
        return "Hard Majority"

    def author(self):
        return "******"