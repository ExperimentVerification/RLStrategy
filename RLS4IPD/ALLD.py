#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Always Defect(ALLD): Defects on every move.
from Strategy import *

class ALLD(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)

    def respond(self, game):
        return 'D'

    def name(self):
        return "Always Defects"

    def author(self):
        return "******"