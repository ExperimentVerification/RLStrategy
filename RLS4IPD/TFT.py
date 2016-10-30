#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tit for Tat(TFT): Cooperates on the first move, then copies the opponent's last move.
from Strategy import *

class TFT(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)

    def respond(self, game):
        if self.getLastResponsePair() == 0:
            return 'C'
        else:
            return self.getLastResponsePair()[1]

    def name(self):
        return "Tit for Tat"

    def author(self):
        return "******"