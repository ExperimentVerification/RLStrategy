#!/usr/bin/env python
# -*- coding: utf-8 -*-

# mem2, behaves like tft in the first two moves, and then shifts among three strategies all_d, tft, tf2t
# according to the interactions with the opponent in the last two moves.
# Rules:
# A, payoff in the last two moves are two Rs, then play tft for the following two moves;
# B, T + S, then play TFTT in the following two moves;
# C, In all other cases, play ALLD in the following two moves;
# D, If ALLD has been chosen twice, always play ALLD.
from Strategy import *

class mem2(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self.payoffLast2 = []
        self.alldTime = 0
        # play for the following two rounds
        self.tft = False
        self.tftt = False
        self.alld = False

        self.oppLast2 = []

    def respond(self, game):
        if self.getLastResponsePair() == 0:
            return 'C'
        else:

            OppLast = self.getLastResponsePair()[1]
            MyLast = self.getLastResponsePair()[0]

            if MyLast == 'C' and OppLast == 'C':
                payoff = 'R'
            elif MyLast == 'C' and OppLast == 'D':
                payoff = 'S'
            elif MyLast == 'D' and OppLast == 'C':
                payoff = 'T'
            elif MyLast == 'D' and OppLast == 'D':
                payoff = 'P'

            self.payoffLast2.append(payoff)
            self.oppLast2.append(OppLast)

            if len(self.payoffLast2) < 2:
                # play tft in the second move
                return OppLast
            else:
                # from the third move
                a = self.payoffLast2[0]
                b = self.payoffLast2[1]
                c = self.oppLast2[0]
                d = self.oppLast2[1]
                self.payoffLast2.pop(0)
                self.oppLast2.pop(0)

                if self.alldTime < 2:
                    if self.tft:
                        self.tft = False
                        return OppLast

                    if self.tftt:
                        self.tftt = False
                        if c == 'D' and d == 'D':
                            return 'D'
                        else:
                            return 'C'

                    if self.alld:
                        self.alld = False
                        return 'D'


                    if a == 'R' and b == 'R':
                        self.tft = True
                        return OppLast
                    elif (a == 'T' and b == 'S') or (a == 'S' and b == 'T'):
                        self.tftt = True
                        if c == 'D' and d == 'D':
                            return 'D'
                        else:
                            return 'C'
                    else:
                        self.alld = True
                        self.alldTime += 1
                        return 'D'
                else:
                    return 'D'

    def name(self):
        return "Memory 2"

    def author(self):
        return "******"