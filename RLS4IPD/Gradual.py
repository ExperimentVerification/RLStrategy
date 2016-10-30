#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Gradual: Cooperates on the first move, and cooperates as long as the opponent cooperates.
# After the first defection of the other player, it defects one time and cooperates two times; ...
# After the nth defection it reacts with n consecutive defections and then clams down its opponent with two cooperations.
from Strategy import *

class Gradual(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self.punish = False
        self.calm = False
        self.numOppDef = 0
        self.defectionC = 0
        # self.cooperationC = 0

    def respond(self, game):
        if self.getLastResponsePair() == 0:
            return 'C'
        else:

            if self.calm:
                self.calm = False
                return 'C'

            if self.punish:
                if self.defectionC < self.numOppDef:
                    self.defectionC += 1
                    return 'D'
                else:
                    self.calm = True
                    self.punish = False
                    self.defectionC += 1
                    return 'C'

            if self.getLastResponsePair()[1] == 'D':
                self.punish = True
                self.defectionC = 1
                self.numOppDef += 1
                return 'D'

            return 'C'


    def name(self):
        return "Gradual"

    def author(self):
        return "******"