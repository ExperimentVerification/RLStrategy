#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Lambda import *
from Games import *
import abc
import random

# definition of the abstract class of the DGPD Strategy
class Strategy(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._lambda = ''
        self.__rounds = 0
        self.__gameHistory = []
        self.__setMaterialSc(0.0)
        self.__setSocialSc(0.0)
        # self.__opponent = ''

    def __str__(self):
        return self.name()

    # set the opponent strategy
    def setOpponent(self, oppo):
        self.__opponent = oppo

    # set the social score to the value of the arg
    def __setSocialSc(self, sScore):
        self.__socialScore = sScore

    # set the material score to the value of the arg
    def __setMaterialSc(self, mScore):
        self.__materialScore = mScore

    # update the histories for both sides
    def updateHistory(self, resp):
        self.setHistory(0, resp)
        # print self.__gameHistory
        self.__opponent.setHistory(1, resp)
        # print self.__opponent.__gameHistory

    # for adding new responses
    def setHistory(self, index, resp):
        # createNew = False
        if self.__rounds % 200 == 0 and self.__opponent.__rounds % 200 == 0:
            createNew = True
        else:
            # print self.__gameHistory
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

    # get the opponent
    # def getOpponent(self):
    #     return self.__opponent

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

    def getLastLambda(self):
        publicLambda = -999
        if self.__rounds > 1:
            publicLambda = self._lambda.getHistory
        return publicLambda

    def getSocialSc(self):
        return self.__socialScore

    def getMaterialSc(self):
        return self.__materialScore

    def getRoundsPlayed(self):
        return self.__rounds

    # abstract method respond to be implemented in the detailed strategy
    @abc.abstractmethod
    def respond(self, game):
        """Respond must be implemented."""

    # play the game for one round
    def play(self, game):
        res = self.respond(game)
        self.updateHistory(res)
        self.__rounds += 1

    # calculate the scores
    def calculateScore(self, games):
        if len(self.getLastResponsePair()) != 0:
            lastResponse = tuple(self.getLastResponsePair())
            self.__setSocialSc(self.getSocialSc() + self._lambda.getValue() * games.Games[1].get(lastResponse)[0])
            self.__setMaterialSc(self.getMaterialSc()+ (1 - self._lambda.getValue()) * games.Games[0].get(lastResponse)[0])

    @abc.abstractmethod
    def name(self):
        """Strategy name must be returned."""

    @abc.abstractmethod
    def author(self):
        """Strategy author must be returned."""

    # NE for the DGPD given a social coefficient value
    @staticmethod
    def NashEquilibrium(lambdA):
        if lambdA.getValue() == 0.0:
            return 'D'
        elif lambdA.getValue() <= 0.1:
            return 'D'
        elif lambdA.getValue() <= 0.2:
            return 'D'
        elif lambdA.getValue() <= 0.3:
            if random.randint(1, 10) > 3:
                return 'D'
            else:
                return 'C'
        elif lambdA.getValue() <= 0.4:
            if random.randint(1, 10) > 3:
                return 'D'
            else:
                return 'C'
        elif lambdA.getValue() <= 0.5:
            return 'C'
        elif lambdA.getValue() <= 0.6:
            return 'C'
        elif lambdA.getValue() <= 0.7:
            return 'C'
        elif lambdA.getValue() <= 0.8:
            return 'C'
        elif lambdA.getValue() <= 0.9:
            return 'C'
        elif lambdA.getValue >= 1.0:
            return 'C'
        return ''