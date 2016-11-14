#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *

# the states in the Q table:
# the parallel action pair or the frequency of parallel cooperation
class ParallelRL(Strategy):
    __QTable = {}
    __Counter = 0

    def __init__(self, game):
        Strategy.__init__(self)
        self.__LastState = -999
        self.__LastAction = -999
        self.__CurrentState = -999
        self.__CurrentAction = -999
        self.__ExplorePercentage = 5.0

        self.__oppLastN = []
        self.__myLastN = []
        self.__OppC = 0
        self.__OppD = 0
        self.historyLastN = [] # store the past n rounds records


    def respond(self, game):
        ParallelRL.__Counter += 1
        if self.getLastResponsePair() == 0:
            return 'C'
        else:
            MyLast = self.getLastResponsePair()[0]
            OppLast = self.getLastResponsePair()[1]
            if OppLast == 'C':
                self.__OppC += 1
            else:
                self.__OppD += 1

            self.historyLastN.append((MyLast, OppLast))
            self.__oppLastN.append(OppLast)
            self.__myLastN.append(MyLast)

            if len(self.historyLastN) < game.RL_memLen: # n for last n rounds
                # play tft before the first state is formed
                return OppLast
            else:
                if self.__LastState == -999:
                    # different action choices

                    # parallel action pairs - PAP
                    # self.__LastState = tuple(self.historyLastN)

                    # frequency of parallel cooperation - FPC
                    self.__LastState = (str(self.__myLastN.count('C')), str(self.__oppLastN.count('C')))

                    # FPC+OCP
                    # self.__LastState = (str(self.__myLastN.count('C')), str(self.__oppLastN.count('C')), int(self.__OppC/self.getRoundsPlayed() * 10))
                    if self.__LastState not in ParallelRL.__QTable:
                        ParallelRL.__QTable[self.__LastState] = [0, 0]

                    self.__LastAction = self.getBestAction(self.__LastState, game)
                    if self.__LastAction == 0:
                        FinalDecision = 'C'
                    else:
                        FinalDecision = 'D'
                else:
                    self.historyLastN.pop(0)
                    self.__oppLastN.pop(0)
                    # Q-Table states

                    # self.__CurrentState = tuple(self.historyLastN) # PAP

                    self.__CurrentState = (str(self.__myLastN.count('C')), str(self.__oppLastN.count('C'))) # FPC

                    # self.__CurrentState = (str(self.__myLastN.count('C')), str(self.__oppLastN.count('C')), int(self.__OppC / self.getRoundsPlayed() * 10)) # FPC+OCP

                    FinalDecision = self.learningResult(OppLast, game)
            return FinalDecision

    def learningResult(self, OppLastAction, game):
        # get the reward
        Reward = self.getReward(OppLastAction, game)

        if self.__CurrentState not in ParallelRL.__QTable:
            ParallelRL.__QTable[self.__CurrentState] = [0, 0]

        self.__CurrentAction = self.getBestAction(self.__CurrentState, game)

        # Q-Table updating
        ParallelRL.__QTable[self.__LastState][self.__LastAction] += game.RL_lR * (Reward + game.RL_disF *
                                                                               ParallelRL.__QTable[self.__CurrentState][self.__CurrentAction] -
                                                                               ParallelRL.__QTable[self.__LastState][self.__LastAction])

        self.__LastState = self.__CurrentState
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

        return GAME.pd.get((my, OppLast))[0] - 2 # negative rewards

    def getBestAction(self, state, game):
        self.__ExplorePercentage = -(5.0 / game.Iter_N) * ParallelRL.__Counter + 5

        if random.randint(0, 99) < self.__ExplorePercentage:
            return random.randint(0, 1)
        else:
            if ParallelRL.__QTable[state][0] >= ParallelRL.__QTable[state][1]:
                return 0
            else:
                return 1



    def name(self):
        return "RL based strategy for the IPD with parallel moves"

    def author(self):
        return "******"
