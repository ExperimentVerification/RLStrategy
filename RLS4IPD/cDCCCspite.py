#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cDCCC-spite
from Strategy import *

class cDCCCspite(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)

    def respond(self, game):
        if self.getLastResponsePair() == 0:
            return 'C'
        else:
            MyLast = self.getLastResponsePair()[0]
            OppLast = self.getLastResponsePair()[1]

            if MyLast == 'C'and OppLast == 'C':
                return 'D'
            elif MyLast == 'C'and OppLast == 'D':
                return 'C'
            elif MyLast == 'D'and OppLast == 'C':
                return 'C'
            else:
                return 'C'

    def name(self):
        return "cDCCC-spite"

    def author(self):
        return "******"