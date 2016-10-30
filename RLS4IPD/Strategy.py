#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Games import *
import abc
import random

# definition of the abstract class Strategy
class Strategy(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.__rounds = 0
        self.__gameHistory = []
        self.__setMaterialSc(0.0)

    def __str__(self):
        return self.name()

    # set the opponent strategy
    def setOpponent(self, oppo):
        self.__opponent = oppo


    # set the material score to the value of the arg
    def __setMaterialSc(self, mScore):
        self.__materialScore = mScore

    # update the histories for both sides
    def updateHistory(self, resp, game):
        self.setHistory(0, resp, game)
        # print self.__gameHistory
        self.__opponent.setHistory(1, resp, game)

    # for adding new responses
    def setHistory(self, index, resp, game):
        # createNew = False
        if self.__rounds % game.Iter_N == 0 and self.__opponent.__rounds % game.Iter_N == 0:
            createNew = True
        else:
            if self.__gameHistory[-1][0] == '' or self.__gameHistory[-1][1] == '':
                createNew = False
            else:
                createNew = True

        if createNew:
            NewPair = ['', '']
            self.__gameHistory.append(NewPair)
            self.__gameHistory[-1][index] = resp
        else:
            self.__gameHistory[-1][index] = resp


    # get last rounds action pair
    def getLastResponsePair(self):
        if self.__rounds == 0:
            # first round
            return 0
        else:
            # last round's record
            if self.__gameHistory[-1][0] == '' or self.__gameHistory[-1][1] == '':
                return self.__gameHistory[-2]
            else:
                return self.__gameHistory[-1]
            # return self.__gameHistory[-1]

    def getMaterialSc(self):
        return self.__materialScore

    def getRoundsPlayed(self):
        return self.__rounds

    # abstract method respond to be implemented in the child classes
    @abc.abstractmethod
    def respond(self, game):
        """Respond must be implemented."""

    # play the game for one round
    def play(self, game):
        res = self.respond(game)
        self.updateHistory(res, game)
        self.__rounds += 1

    # calculate the scores
    def calculateScore(self, game):
        if len(self.getLastResponsePair()) != 0 and self.getLastResponsePair()[0] != '' and self.getLastResponsePair()[1] != '':
            lastResponse = tuple(self.getLastResponsePair())
            self.__setMaterialSc(self.getMaterialSc()+ game.pd.get(lastResponse)[0])
            # print self.__materialScore

    @abc.abstractmethod
    def name(self):
        """Strategy name must be returned."""

    @abc.abstractmethod
    def author(self):
        """Strategy author must be returned."""