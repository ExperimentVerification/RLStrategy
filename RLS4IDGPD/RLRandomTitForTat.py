#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *
import random

# the states in the Q table:
# history in the last n rounds - mine and oppo's
# sequential cooperation times - SCT
# state - (my C, oppo's C)
# 3 actions - increase, decrease, nochange
# random TFT for decision making
class RLRandomTitForTat(Strategy):
    __QTable4L = {}
    __Counter = 0
    __LastLambda = 0.0
    __CoopRatio = 0.3

    def __init__(self, game):
        Strategy.__init__(self)

        # parameter updating
        self.__LastState4L = -999
        self.__LastAction4L = -999
        self.__CurrentState4L = -999
        self.__CurrentAction4L = -999

        self.__ExplorePercentage = 5.0

        # optionally random an initial lambda
        # self._lambda = Lambda(0.0)
        self._lambda = Lambda(random.random())

        self.myCtr = 0
        self.oppCtr = 0


        # state constructing parameters
        self.__mybeforeLastN = []
        self.__oppLastN = []
        self.__mybeforeLast = []
        self.__OppC = 0

        RLRandomTitForTat.__Counter = 0


    def respond(self, game):
        RLRandomTitForTat.__Counter += 1
        if self.getLastResponsePair() == 0:
            # cooperate for the first round'
            self._lambda.nochange()
            self.__LastAction4L = 0
            RLRandomTitForTat.__LastLambda = round(self._lambda.getValue(), 1)
            if random.randint(0, 9) % 2 == 0:
                return 'D'
            else:
                return 'C'
        else:
            MyLast = self.getLastResponsePair()[0]
            OppLast = self.getLastResponsePair()[1]

            if OppLast == 'C':
                self.__OppC += 1

            if len(self.__mybeforeLast) < 2:
                self.__mybeforeLast.append(MyLast)
            else:
                self.__mybeforeLast.pop(0)
                self.__mybeforeLast.append(MyLast)

            self.__oppLastN.append(OppLast)
            if len(self.__mybeforeLast) > 1:
                self.__mybeforeLastN.append(self.__mybeforeLast[0])

            if len(self.__mybeforeLastN) < game.RL_memLen: # memory length = n
                # play TFT for the 2-n round
                self._lambda.nochange()
                if random.randint(0, 9) % 2 == 0:
                    return 'D'
                else:
                    return 'C'
            else:
                if self.__LastState4L == -999:
                    # construct the first state
                    self.__oppLastN.pop(0)

                    self.__CurrentState4L = (str(self.__mybeforeLastN.count('C')), str(self.__oppLastN.count('C')))
                    if self.__CurrentState4L not in RLRandomTitForTat.__QTable4L:
                        RLRandomTitForTat.__QTable4L[self.__CurrentState4L] = [0, 0, 0]

                    self.__CurrentAction4L = self.getBestChange(self.__CurrentState4L, game)
                    self.__LastState4L = self.__CurrentState4L
                    self.__LastAction4L = self.__CurrentAction4L
                    self.updateLambda(self.__CurrentAction4L)

                    if random.randint(0, 9) % 2 == 0:
                        return 'D'
                    else:
                        return 'C'

                else:
                    # from the next round, begin Q-Table updating
                    self.__oppLastN.pop(0)
                    self.__mybeforeLastN.pop(0)

                    self.__CurrentState4L = (str(self.__mybeforeLastN.count('C')), str(self.__oppLastN.count('C')))
                    self.learningResult4L(OppLast, MyLast, game)

            RLRandomTitForTat.__LastLambda = round(self._lambda.getValue(), 1)
            if random.randint(0, 9) % 2 == 0:
                return 'D'
            else:
                return 'C'


    def learningResult4L(self, OppLastAction, MyLastAction, game):
        Reward4L = self.getReward(OppLastAction, MyLastAction, game)
        if self.__CurrentState4L not in RLRandomTitForTat.__QTable4L:
            RLRandomTitForTat.__QTable4L[self.__CurrentState4L] = [0, 0, 0]

        self.__CurrentAction4L = self.getBestChange(self.__CurrentState4L, game)

        RLRandomTitForTat.__QTable4L[self.__LastState4L][self.__LastAction4L] += game.RL_lR * \
                                                                                 (Reward4L + game.RL_disF * RLRandomTitForTat.__QTable4L[self.__CurrentState4L][self.__CurrentAction4L] -
                                                                                  RLRandomTitForTat.__QTable4L[self.__LastState4L][self.__LastAction4L])

        self.__LastState4L = self.__CurrentState4L
        self.__LastAction4L = self.__CurrentAction4L

        self.updateLambda(self.__CurrentAction4L)

    def getReward(self, OppLast, MyLast, GAME):
        valLambda = float(RLRandomTitForTat.__LastLambda)

        return (GAME.Games[0].get((MyLast, OppLast))[0] * (1.0 - valLambda) + GAME.Games[1].get((MyLast, OppLast))[0] * valLambda) - 3


    def getBestChange(self, state, game):
        self.__ExplorePercentage = -(5.0 / game.Iter_N) * RLRandomTitForTat.__Counter + 5

        if random.randint(0, 99) < self.__ExplorePercentage:
            return random.randint(0, 2)
        else:
            return RLRandomTitForTat.__QTable4L[state].index(max(RLRandomTitForTat.__QTable4L[state]))


    def updateLambda(self, actionNumber):
        if actionNumber == 0:
            self._lambda.nochange()
        elif actionNumber == 1:
            self._lambda.decrementValue()
        else:
            self._lambda.incrementValue()

    def name(self):
        return "RL-based random TFT - update parameter based on the QTable, and make random decisions"

    def author(self):
        return "******"