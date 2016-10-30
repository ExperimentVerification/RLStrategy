#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *

# single state s, no change
# no sensation
class SingleState(Strategy):
    __QTable = []
    __Counter = 0
    __CoopRatio = 0.3

    def __init__(self, game):
        Strategy.__init__(self)
        self.__LastAction = -999
        self.__CurrentAction = -999
        self.__ExplorePercentage = 5.0
        self.initialiseQ(game)


    def respond(self, game):
        SingleState.__Counter += 1

        if self.getLastResponsePair() == 0:
            # cooperate for the first round'
            self.__LastAction = 0
            return 'C'
        else:
            # MyLast = self.getLastResponsePair()[0]
            OppLast = self.getLastResponsePair()[1]
            FinalDecision = self.learningResult(OppLast, game)
            return FinalDecision

    def learningResult(self, OppLastAction, game):
        Reward = self.getReward(OppLastAction, game)

        self.__CurrentAction = self.getBestAction(game)

        SingleState.__QTable[self.__LastAction] += game.RL_lR * (Reward + game.RL_disF *
        SingleState.__QTable[self.__CurrentAction] -
        SingleState.__QTable[self.__LastAction])

        # self.__LastState = self.__CurrentState
        self.__LastAction = self.__CurrentAction

        if self.__CurrentAction == 0:
            return 'C'
        else:
            return 'D'

    def getReward(self, OppLast, GAME):
        if self.__LastAction == 0:
            my = 'C'
        else:
            my = 'D'

        return GAME.pd.get((my, OppLast))[0] - 2

    def getBestAction(self, game):
        self.__ExplorePercentage = -(5.0 / game.Iter_N) *  SingleState.__Counter + 5

        if random.randint(0, 99) < self.__ExplorePercentage:
            return random.randint(0, 1)
        else:
            if SingleState.__QTable[0] > SingleState.__QTable[1]:
                return 0
            else:
                return 1

    def initialiseQ(self, game):
        tmp1 = float(SingleState.__CoopRatio * game.pd.get(('C', 'C'))[0] + (1 - SingleState.__CoopRatio) * game.pd.get(('C', 'D'))[0])
        tmp2 = float(SingleState.__CoopRatio * game.pd.get(('D', 'C'))[0] + (1 - SingleState.__CoopRatio) * game.pd.get(('D', 'D'))[0])
        SingleState.__QTable.append(tmp1)
        SingleState.__QTable.append(tmp2)

    def name(self):
        return "Single State RL-based strategy"

    def author(self):
        return "******"