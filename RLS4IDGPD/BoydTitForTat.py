#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *
# Only play the material game, just like the TFT for the IPD
class BoydTitForTat(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self._lambda = Lambda(0.0) # play the material game only

    def respond(self, game):
        if self.getLastResponsePair() == 0:
            self._lambda.nochange()
            return 'C'
        elif self.getLastResponsePair()[1] == 'C':
            self._lambda.nochange()
            return 'C'
        else:
            self._lambda.nochange()
            return 'D'

    def name(self):
        return "Tit-For-Tat from Boyd's Tournament"

    def author(self):
        return "In-house (Theodore Boyd)"