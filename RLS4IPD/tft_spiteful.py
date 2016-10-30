#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 4/4 4 new strategies: tft_spiteful, starts with a c, then play tft unless sha has been betrayed two times consecutively,
# in which case she always betrays
from Strategy import *

class tft_spiteful(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self.oppLast2 = []
        self.allD = False

    def respond(self, game):
        if self.getLastResponsePair() == 0:
            return 'C'
        else:
            OppLast = self.getLastResponsePair()[1]
            self.oppLast2.append(OppLast)

            if len(self.oppLast2) < 2:
                # play tft for the second round
                return OppLast
            else:
                if self.oppLast2[0] == 'D' and self.oppLast2[1] == 'D':
                    self.allD = True


                self.oppLast2.pop(0)

                if self.allD:
                    return 'D'
                else:
                    return OppLast



    def name(self):
        return "tft_spiteful"

    def author(self):
        return "******"