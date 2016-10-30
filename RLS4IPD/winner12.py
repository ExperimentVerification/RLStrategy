#!/usr/bin/env python
# -*- coding: utf-8 -*-

# winner12(mem12_ccCDCDDCDD)
from Strategy import *

class winner12(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self.myLast = ''
        self.oppLast2 = []

    def respond(self, game):
        if self.getLastResponsePair() == 0:
            return 'C'
        else:
            self.myLast = self.getLastResponsePair()[0]
            self.oppLast2.append(self.getLastResponsePair()[1])
            if len(self.oppLast2) < 2:
                return 'C'
            else:
                res = 'C'
                if self.myLast == 'C':
                    res = self.getLastResponsePair()[1]
                else:
                    res = self.oppLast2[0]
                    if self.oppLast2[1] == 'C':
                        res = 'D'
            self.oppLast2.pop(0)
            return res


    def name(self):
        return "mem12_ccCDCDDCDD"

    def author(self):
        return "******"