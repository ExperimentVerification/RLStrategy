#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Soft Majority(SM): Cooperates on the first move, and cooperates as long as the number of times the opponent has cooperated
# is greater than or equal to the number of times it has defected, else it defects.
from Strategy import *

class SM(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self.OppC = 0
        self.OppD = 0

    def respond(self, game):
        if self.getLastResponsePair() == 0:
            return 'C'
        else:
            if self.getLastResponsePair()[1] == 'D':
                self.OppD += 1
            else:
                self.OppC += 1

            if self.OppC >= self.OppD:
                return 'C'
            else:
                return 'D'


    def name(self):
        return "Soft Majority"

    def author(self):
        return "******"