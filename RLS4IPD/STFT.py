#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Suspicious Tit for Tat(STFT): Same as TFT, except that it defects on the first move.
from Strategy import *

class STFT(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)

    def respond(self, game):
        if self.getLastResponsePair() == 0:
            return 'D'
        else:
            return self.getLastResponsePair()[1]

    def name(self):
        return "Suspicious Tit for Tat"

    def author(self):
        return "******"