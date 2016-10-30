#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 3/4 4 new strategies: spiteful_cc, classical spiteful with a cc forced start
from Strategy import *

class spiteful_cc(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self.counter = 0

    def respond(self, game):
        if self.getLastResponsePair() == 0:
            return 'C'
        else:
            if self.counter < 1:
                # cc to start
                self.counter += 1
                return 'C'
            elif self.getLastResponsePair()[0] == 'C' and self.getLastResponsePair()[1] == 'C':
                return 'C'
            else:
                return 'D'

    def name(self):
        return "spiteful_cc"

    def author(self):
        return "******"