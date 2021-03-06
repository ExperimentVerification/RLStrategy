#!/usr/bin/env python
# -*- coding: utf-8 -*-

# dDCCC-spite
from Strategy import *

class dDCCCspite(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)

    def respond(self, game):
        if self.getLastResponsePair() == 0:
            return 'D'
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
        return "dDCCC-spite"

    def author(self):
        return "******"