#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *
# RL-version see RLAEGS
class BoydRafalStrategy(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self._lambda = Lambda(0.0)
        self.__Dict = {}
        self.__Dict[('C', 'C')] = 0
        self.__Dict[('C', 'D')] = 0
        self.__Dict[('D', 'C')] = 0
        self.__Dict[('D', 'D')] = 0

    def respond(self, game):
        if self.getRoundsPlayed() != 0:
            if self.getLastResponsePair()[0] != '' and self.getLastResponsePair()[1] != '':
                self.__Dict[tuple(self.getLastResponsePair())] += 1

                if max(self.__Dict) == ('D', 'C'):
                    # if the player has get the T for many times, decrease the weight on the SG
                    self._lambda.decrementValue()
                else:
                    self._lambda.incrementValue()
        else:
            self._lambda.nochange()

        return Strategy.NashEquilibrium(self._lambda)

    def name(self):
        return "Rafal Strategy from Boyd's Tournament"

    def author(self):
        return "Rafal Szymanski"