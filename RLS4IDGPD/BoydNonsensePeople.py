#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *
# play with a random constant social coefficient
class BoydNonsensePeople(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self._lambda = Lambda(random.random())

    def respond(self, game):
        self._lambda.nochange()
        return Strategy.NashEquilibrium(self._lambda)

    def name(self):
        return "Nonsense People from Boyd's Tournament"

    def author(self):
        return "In-house (Ali Ghoroghi)"