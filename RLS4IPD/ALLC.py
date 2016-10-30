#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Always Cooperate(ALLC): Cooperates on every move.
from Strategy import *

class ALLC(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)

    def respond(self, game):
        return 'C'

    def name(self):
        return "Always Cooperate"

    def author(self):
        return "******"
