#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *
from Lambda import *
import random


class BoydSocialTitForTat(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self._lambda = Lambda(random.random()) # random initialisation for the lambda

    def respond(self, game):
        if self.getRoundsPlayed() == 0:
            self._lambda.nochange()
            return 'C'
        else:
            # from the second round
            if self.getLastResponsePair()[1] == 'C':
                self._lambda.incrementValue()
                return 'C'
            else:
                self._lambda.decrementValue()
                return 'D'


    def name(self):
        return "Social Tit For Tat from Boyd's Tournament"

    def author(self):
        return "In-house (Theodore Boyd)"