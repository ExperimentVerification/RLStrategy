#!/usr/bin/env python
# -*- coding: utf-8 -*-

# winner21(mem21_dcCDCDCDDD)
from Strategy import *

class winner21(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self.myLast2 = []
        self.oppLast = ''

    def respond(self, game):
        if self.getLastResponsePair() == 0:
            return 'D'
        else:
            self.oppLast = self.getLastResponsePair()[1]
            self.myLast2.append(self.getLastResponsePair()[0])
            if len(self.myLast2) < 2:
                return 'C'
            else:
                res = 'C'
                if self.myLast2[0] == 'C' or self.myLast2[1] == 'C':
                    res = self.getLastResponsePair()[1]
                else:
                    res = 'D'

            self.myLast2.pop(0)
            return res


    def name(self):
        return "mem21_dcCDCDCDDD"

    def author(self):
        return "******"