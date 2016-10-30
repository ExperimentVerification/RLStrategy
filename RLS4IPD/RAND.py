#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Random Player(RAND): Makes a random move with even chance for C and D
from Strategy import *
import random

class RAND(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)

    def respond(self, game):
        if random.random() < 0.5:
            return 'C'
        else:
            return 'D'

    def name(self):
        return "Random Player"

    def author(self):
        return "******"