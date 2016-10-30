#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Score():
    def __init__(self, n, a, o):
        self.name = n
        self.author = a
        self.opponentName = o
        self.runsMade = 0
        self.lambdA = 0.0
        self.materialScore = 0.0
        self.socialScore = 0.0
        self.aggregates = 0.0
