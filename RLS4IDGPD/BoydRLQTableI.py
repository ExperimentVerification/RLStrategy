#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *
from Lambda import *
import random

# state: 0.0, 0.2, 0.4, 0.6, 0.8, 1.0
# action: C and D
class BoydRLQTableI(Strategy):
    __QTable = [] # actions 2 - C and D, states, only need 6 states
    __Counter = 0;
    __LastLambda = 0.0
    __CoopRatio = 0.3 # Poc, the probability of the opponent to cooperate

    def __init__(self, game):
        Strategy.__init__(self)
        self.__LastState = -999
        self.__LastAction = -999
        self.__CurrentState = -999
        self.__CurrentAction = -999

        self._lambda = Lambda(BoydRLQTableI.__CoopRatio)
        self.initialQ(game)  # initialise the Q-Table with the formulas
        BoydRLQTableI.__Counter = 0
        self.__ExplorePercentage = 5.0 # for epsilon-greedy
        BoydRLQTableI.__LastLambda = BoydRLQTableI.__CoopRatio


    def respond(self, game):
        BoydRLQTableI.__Counter += 1

        if self.getRoundsPlayed() == 0:
            # for the first round
            self._lambda.nochange()
            self.__LastState = round(self._lambda.getValue(), 1)
            self.__LastAction = 0
            BoydRLQTableI.__LastLambda = round(self._lambda.getValue(), 1)
            return 'C'
        else:
            OppLast = self.getLastResponsePair()[1]
            MyLast = self.getLastResponsePair()[0]

            # parameter updating
            if MyLast == 'C' and OppLast == 'C':
                self._lambda.decrementValue()
            elif MyLast == 'C' and OppLast == 'D':
                self._lambda.incrementValue()
            elif MyLast == 'D' and OppLast == 'C':
                self._lambda.decrementValue()
            elif MyLast == 'D' and OppLast == 'D':
                self._lambda.incrementValue()

            # decision making with RL Q-Table
            self.__CurrentState = round(self._lambda.getValue(), 1)
            FinalDecision = self.learningResult(OppLast, game)
            BoydRLQTableI.__LastLambda = round(self._lambda.getValue(), 1)

            return FinalDecision

    def learningResult(self, OppLastAction, game):
        # get reward from the payoff for the last round
        Reward = self.getReward(OppLastAction, game)
        self.__CurrentAction = self.getBestAction(self.__CurrentState, game)

        # right version of the Q-Value updating formula
        BoydRLQTableI.__QTable[int(self.__LastState/0.2)][self.__LastAction] += game.RL_lR * \
                                                                                (Reward + game.RL_disF * BoydRLQTableI.__QTable[int(self.__CurrentState/0.2)][self.__CurrentAction]-
                                                                                 BoydRLQTableI.__QTable[int(self.__LastState/0.2)][self.__LastAction])


        self.__LastState = self.__CurrentState
        self.__LastAction = self.__CurrentAction

        if self.__CurrentAction == 0:
            return 'C'
        else:
            return 'D'

    def getBestAction(self, state, game):
        self.__ExplorePercentage = -(5.0 / game.Iter_N) * BoydRLQTableI.__Counter + 5

        if random.randint(0, 99) < self.__ExplorePercentage:
            return random.randint(0,1)
        else:
            if BoydRLQTableI.__QTable[int(state/0.2)][0] >= BoydRLQTableI.__QTable[int(state/0.2)][1]:
                return 0
            else:
                return 1

    def getReward(self, OppLast, GAME):
        valLambda = float(BoydRLQTableI.__LastLambda)
        if self.__LastAction == 0:
            my = 'C'
        else:
            my = 'D'

        return GAME.Games[0].get((my, OppLast))[0] * (1.0 - valLambda) + GAME.Games[1].get((my, OppLast))[0] * valLambda

    def initialQ(self, game):
        for i in range(0,6):
            lambda1 = round(i * 0.2, 1)

            temp1 = float(BoydRLQTableI.__CoopRatio * (game.Games[0].get(('C', 'C'))[0] * (1.0 - lambda1) + game.Games[1].get(('C', 'C'))[0] * lambda1) +
                          (1.0 - BoydRLQTableI.__CoopRatio) * (game.Games[0].get(('C', 'D'))[0] * (1.0 - lambda1) + game.Games[1].get(('C', 'D'))[0] * lambda1))
            temp2 = float(BoydRLQTableI.__CoopRatio * (game.Games[0].get(('D', 'C'))[0] * (1.0 - lambda1) + game.Games[1].get(('D', 'C'))[0] * lambda1)+
                          (1.0 - BoydRLQTableI.__CoopRatio) * (game.Games[0].get(('D', 'D'))[0] * (1.0 - lambda1) + game.Games[1].get(('D', 'D'))[0] * lambda1))

            BoydRLQTableI.__QTable.append([temp1, temp2])

    def name(self):
        return "RL QTable I from Boyd's Tournament"

    def author(self):
        return "Alex Gao"