#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *
from Lambda import *
import random
# Bod's improvement on Gao's method
# emphasizing on the parameter selection and reward function desigh
class BoydRLQTableIPlus(Strategy):
    __QTable = [] # actions 2 - C and D, states, only need 6 states
    __Counter = 0;
    __LastLambda = 0.0
    __CoopRatio = 0.3 # Poc, the probability of the opponent to cooperate
    __learningRate = 0.1
    __discountFactor = 0.9
    __ccLambdaA = 3
    __ccLambdaB =2.5
    __cdLambda = 2.5
    __dcLambda = 5
    __ddLambda = 1
    __gamma = 0.5


    def __init__(self, game):
        Strategy.__init__(self)
        self.__LastState = -999
        self.__LastAction = -999
        self.__CurrentState = -999
        self.__CurrentAction = -999

        BoydRLQTableIPlus.__gamma = game.Lambda_global
        gammaSwitch = int(BoydRLQTableIPlus.__gamma * 10)
        if gammaSwitch == 0:
            BoydRLQTableIPlus.__CoopRatio = 0.0
            BoydRLQTableIPlus.__learningRate = 0.0
            BoydRLQTableIPlus.__discountFactor = 0.0
            BoydRLQTableIPlus.__ccLambdaA = 0.0
            BoydRLQTableIPlus.__ccLambdaB = 4.0
            BoydRLQTableIPlus.__cdLambda = 4.0
            BoydRLQTableIPlus.__dcLambda = 10.0
            BoydRLQTableIPlus.__ddLambda = 10.0
        elif gammaSwitch == 2:
            BoydRLQTableIPlus.__CoopRatio = 0.0
            BoydRLQTableIPlus.__learningRate = 0.5
            BoydRLQTableIPlus.__discountFactor = 0.0
            BoydRLQTableIPlus.__ccLambdaA = 4.0
            BoydRLQTableIPlus.__ccLambdaB = 0.0
            BoydRLQTableIPlus.__cdLambda = 0.0
            BoydRLQTableIPlus.__dcLambda = 10.0
            BoydRLQTableIPlus.__ddLambda = 10.0
        elif gammaSwitch == 4:
            BoydRLQTableIPlus.__CoopRatio = 0.5
            BoydRLQTableIPlus.__learningRate = 1.0
            BoydRLQTableIPlus.__discountFactor = 0.5
            BoydRLQTableIPlus.__ccLambdaA = 10.0
            BoydRLQTableIPlus.__ccLambdaB = 4.0
            BoydRLQTableIPlus.__cdLambda = 0.0
            BoydRLQTableIPlus.__dcLambda = 0.0
            BoydRLQTableIPlus.__ddLambda = 10.0
        elif gammaSwitch == 6:
            BoydRLQTableIPlus.__CoopRatio = 0.5
            BoydRLQTableIPlus.__learningRate = 0.5
            BoydRLQTableIPlus.__discountFactor = 0.5
            BoydRLQTableIPlus.__ccLambdaA = 2.0
            BoydRLQTableIPlus.__ccLambdaB = 2.0
            BoydRLQTableIPlus.__cdLambda = 4.0
            BoydRLQTableIPlus.__dcLambda = 0.0
            BoydRLQTableIPlus.__ddLambda = 0.0
        elif gammaSwitch == 8:
            BoydRLQTableIPlus.__CoopRatio = 1.0
            BoydRLQTableIPlus.__learningRate = 1.0
            BoydRLQTableIPlus.__discountFactor = 1.0
            BoydRLQTableIPlus.__ccLambdaA = 10.0
            BoydRLQTableIPlus.__ccLambdaB = 4.0
            BoydRLQTableIPlus.__cdLambda = 10.0
            BoydRLQTableIPlus.__dcLambda = 0.0
            BoydRLQTableIPlus.__ddLambda = 0.0
        elif gammaSwitch == 10:
            BoydRLQTableIPlus.__CoopRatio = 1.0
            BoydRLQTableIPlus.__learningRate = 1.0
            BoydRLQTableIPlus.__discountFactor = 0.0
            BoydRLQTableIPlus.__ccLambdaA = 10.0
            BoydRLQTableIPlus.__ccLambdaB = 8.0
            BoydRLQTableIPlus.__cdLambda = 0.0
            BoydRLQTableIPlus.__dcLambda = 0.0
            BoydRLQTableIPlus.__ddLambda = 4.0


        self._lambda = Lambda(BoydRLQTableIPlus.__CoopRatio)
        self.initialQ(game) # initialise the Qtable
        BoydRLQTableIPlus.__Counter = 0
        self.__ExplorePercentage = 0.0  # for epsilon-greedy, epsilon = 0
        BoydRLQTableIPlus.__LastLambda = BoydRLQTableIPlus.__CoopRatio


    def respond(self, game):
        BoydRLQTableIPlus.__Counter += 1
        if self.getRoundsPlayed() == 0:
            # for the first round
            self._lambda.nochange()
            self.__LastState = round(self._lambda.getValue(), 1)
            self.__LastAction = 0
            BoydRLQTableIPlus.__LastLambda = round(self._lambda.getValue(), 1)
            return 'C'
        else:
            # from the second round
            OppLast = self.getLastResponsePair()[1]
            MyLast = self.getLastResponsePair()[0]

            if MyLast == 'C' and OppLast == 'C':
                self._lambda.decrementValue()
            elif MyLast == 'C' and OppLast == 'D':
                self._lambda.incrementValue()
            elif MyLast == 'D' and OppLast == 'C':
                self._lambda.decrementValue()
            elif MyLast == 'D' and OppLast == 'D':
                self._lambda.incrementValue()

            self.__CurrentState = round(self._lambda.getValue(), 1)
            FinalDecision = self.learningResult(OppLast, game)
            BoydRLQTableIPlus.__LastLambda = self._lambda.getValue()

            return FinalDecision

    def learningResult(self, OppLastAction, game):

        Reward = self.getReward(OppLastAction, game)
        self.__CurrentAction = self.getBestAction(self.__CurrentState, game)

        BoydRLQTableIPlus.__QTable[int(self.__LastState/0.2)][self.__LastAction] += \
            game.RL_lR * (Reward + game.RL_disF * (BoydRLQTableIPlus.__QTable[int(self.__CurrentState/0.2)][self.__CurrentAction]- BoydRLQTableIPlus.__QTable[int(self.__LastState/0.2)][self.__LastAction]))
        # BoydRLQTableIPlus.TrainedQ = BoydRLQTableIPlus.__QTable

        self.__LastState = self.__CurrentState
        self.__LastAction = self.__CurrentAction

        if self.__CurrentAction == 0:
            return 'C'
        else:
            return 'D'

    def getBestAction(self, state, game):
        self.__ExplorePercentage = -(5.0 / game.Iter_N) * BoydRLQTableIPlus.__Counter + 5

        if random.randint(0, 99) < self.__ExplorePercentage:
            return random.randint(0,1)
        else:
            if BoydRLQTableIPlus.__QTable[int(state/0.2)][0] >= BoydRLQTableIPlus.__QTable[int(state/0.2)][1]:
                return 0
            else:
                return 1

    def getReward(self, OppLast, GAME):
        # use the selected parameters
        valLambda = float(BoydRLQTableIPlus.__LastLambda)
        if OppLast == 'C':
            opL = 0
        else:
            opL = 1

        if self.__LastAction == 0 and opL == 0:
            return BoydRLQTableIPlus.__ccLambdaA * (1.0 - valLambda) + BoydRLQTableIPlus.__ccLambdaB * valLambda
        elif self.__LastAction == 0 and opL == 1:
            return BoydRLQTableIPlus.__cdLambda * valLambda
        elif self.__LastAction == 1 and opL == 0:
            return BoydRLQTableIPlus.__dcLambda * (1.0 - valLambda)
        else:
            return BoydRLQTableIPlus.__ddLambda * (1.0 - valLambda)


    def initialQ(self, game):
        for i in range(0,6):
            lambda1 = round(i * 0.2, 1)

            temp1 = float(BoydRLQTableIPlus.__CoopRatio * (BoydRLQTableIPlus.__ccLambdaA * (1.0 - lambda1) + BoydRLQTableIPlus.__ccLambdaB * lambda1) +
                          (1.0 - BoydRLQTableIPlus.__CoopRatio) * (BoydRLQTableIPlus.__ccLambdaB * lambda1))
            temp2 = float(BoydRLQTableIPlus.__CoopRatio * BoydRLQTableIPlus.__dcLambda * (1.0 - lambda1) + (1.0 - BoydRLQTableIPlus.__CoopRatio) * lambda1)

            BoydRLQTableIPlus.__QTable.append([temp1, temp2])

    def name(self):
        return "RL QTable I+ from Boyd's Tournament"

    def author(self):
        return "Theodore Boyd"