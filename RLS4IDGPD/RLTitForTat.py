#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *

# the states in the Q table:
# history in the last n rounds - mine and oppo's
# sequential cooperation times
# state - (my C, oppo's C)
# without information of the whole history
# 3 actions - increase, decrease, nochange
class RLTitForTat(Strategy):
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

        self._lambda = Lambda(0.0)
        self.myCtr = 0
        self.oppCtr = 0


        # state constructing parameters
        self.__mybeforeLastN = []
        self.__oppLastN = []
        self.__mybeforeLast = []
        self.__OppC = 0

        RLTitForTat.__Counter = 0


    def respond(self, game):
        # print Test10.__Counter
        RLTitForTat.__Counter += 1
        if self.getLastResponsePair() == 0:
            # cooperate for the first round'
            self._lambda.nochange()
            self.__LastAction4L = 0
            RLTitForTat.__LastLambda = round(self._lambda.getValue(), 1)
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
                return OppLast
            else:
                if self.__LastState4L == -999:
                    # construct the first state
                    self.__oppLastN.pop(0)


                    self.__CurrentState4L = (str(self.__mybeforeLastN.count('C')), str(self.__oppLastN.count('C')))
                    if self.__CurrentState4L not in RLTitForTat.__QTable4L:
                        RLTitForTat.__QTable4L[self.__CurrentState4L] = [0, 0, 0]

                    self.__CurrentAction4L = self.getBestChange(self.__CurrentState4L, game)
                    self.__LastState4L = self.__CurrentState4L
                    self.__LastAction4L = self.__CurrentAction4L
                    self.updateLambda(self.__CurrentAction4L)

                    return OppLast

                else:
                    # from the next round, begin Q-Table updating
                    self.__oppLastN.pop(0)
                    self.__mybeforeLastN.pop(0)


                    self.__CurrentState4L = (str(self.__mybeforeLastN.count('C')), str(self.__oppLastN.count('C')))
                    self.learningResult4L(OppLast, MyLast, game)

            RLTitForTat.__LastLambda = round(self._lambda.getValue(), 1)
            return OppLast


    def learningResult4L(self, OppLastAction, MyLastAction, game):
        Reward4L = self.getReward(OppLastAction, MyLastAction, game)
        if self.__CurrentState4L not in RLTitForTat.__QTable4L:
            RLTitForTat.__QTable4L[self.__CurrentState4L] = [0, 0, 0]

        self.__CurrentAction4L = self.getBestChange(self.__CurrentState4L, game)

        RLTitForTat.__QTable4L[self.__LastState4L][self.__LastAction4L] += game.RL_lR * \
                                                                           (Reward4L + game.RL_disF * RLTitForTat.__QTable4L[self.__CurrentState4L][self.__CurrentAction4L] -
                                                                            RLTitForTat.__QTable4L[self.__LastState4L][self.__LastAction4L])

        self.__LastState4L = self.__CurrentState4L
        self.__LastAction4L = self.__CurrentAction4L

        self.updateLambda(self.__CurrentAction4L)

    def getReward(self, OppLast, MyLast, GAME):
        valLambda = float(RLTitForTat.__LastLambda)

        return (GAME.Games[0].get((MyLast, OppLast))[0] * (1.0 - valLambda) + GAME.Games[1].get((MyLast, OppLast))[0] * valLambda) - 3


    def getBestChange(self, state, game):
        self.__ExplorePercentage = -(5.0 / game.Iter_N) * RLTitForTat.__Counter + 5

        if random.randint(0, 99) < self.__ExplorePercentage:
            return random.randint(0, 2)
        else:
            return RLTitForTat.__QTable4L[state].index(max(RLTitForTat.__QTable4L[state]))


    def updateLambda(self, actionNumber):
        if actionNumber == 0:
            self._lambda.nochange()
        elif actionNumber == 1:
            self._lambda.decrementValue()
        else:
            self._lambda.incrementValue()

    def name(self):
        return "RL-based TFT"

    def author(self):
        return "******"