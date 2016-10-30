#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cCDDD-spite
from Strategy import *


class cCDDDspite(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)

    def respond(self, game):
        if self.getLastResponsePair() == 0:
            return 'C'
        else:
            MyLast = self.getLastResponsePair()[0]
            OppLast = self.getLastResponsePair()[1]

            if MyLast == 'C' and OppLast == 'C':
                return 'C'
            elif MyLast == 'C' and OppLast == 'D':
                return 'D'
            elif MyLast == 'D' and OppLast == 'C':
                return 'D'
            else:
                return 'D'

    def name(self):
        return "cCDDD-spite"

    def author(self):
        return "******"