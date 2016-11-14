#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *

# the states in the Q table:
# history in the last n rounds - mine and oppo's
# e.g. state - (my C, oppo's C)
# with or without information of the whole history
# sequential action pairs and sequential cooperation times
class SequentialRL(Strategy):
    __QTable = {}
    __Counter = 0

    def __init__(self, game):
        Strategy.__init__(self)
        self.__LastState = -999
        self.__LastAction = -999
        self.__CurrentState = -999
        self.__CurrentAction = -999
        self.__ExplorePercentage = 5.0

        self.__mybeforeLastN = []
        self.__hisbeforeLastN = []
        self.__oppLastN = []
        self.__mybeforeLast = []
        self.__OppC = 0
        self.__OppD = 0
        self.__MyC = 0
        self.__MyD = 0


    def respond(self, game):
        SequentialRL.__Counter += 1

        if self.getLastResponsePair() == 0:
            # cooperate for the first round'
            self.__LastAction = 0
            return 'C'
        else:
            MyLast = self.getLastResponsePair()[0]
            OppLast = self.getLastResponsePair()[1]

            # for the information of the whole history
            if OppLast == 'C':
                self.__OppC += 1
            else:
                self.__OppD += 1

            if MyLast == 'C':
                self.__MyC += 1
            else:
                self.__MyD += 1

            # keep the lenth of __mybeforeLast 2
            if len(self.__mybeforeLast) < 2:
                self.__mybeforeLast.append(MyLast)
            else:
                self.__mybeforeLast.pop(0)
                self.__mybeforeLast.append(MyLast)

            # append __oppLastN and __mybeforeLastN when __mybeforeLast is not empty
            self.__oppLastN.append(OppLast)
            if len(self.__mybeforeLast) > 1:
                self.__mybeforeLastN.append(self.__mybeforeLast[0])
                self.__hisbeforeLastN.append((self.__mybeforeLast[0], OppLast))


            if len(self.__mybeforeLastN) < game.RL_memLen: # n for n, for opp
                # play TFT for the second to the n+1 round
                return OppLast
            else:
                if self.__LastState == -999:
                    # the n+2 round, construct the first state
                    self.__oppLastN.pop(0)

                    # state options
                    # sequential action pairs - SAP
                    # self.__CurrentState = tuple(self.__hisbeforeLastN)

                    # frequency of sequential cooperation - FSC
                    self.__CurrentState = (str(self.__mybeforeLastN.count('C')), str(self.__oppLastN.count('C')))

                    # FSC+OCP
                    # self.__CurrentState = (str(self.__mybeforeLastN.count('C')), str(self.__oppLastN.count('C')), int(self.__OppC/self.getRoundsPlayed() * 10))

                    if self.__CurrentState not in SequentialRL.__QTable:
                        SequentialRL.__QTable[self.__CurrentState] = [0, 0]

                    self.__CurrentAction = self.getBestAction(self.__CurrentState, game)
                    self.__LastState = self.__CurrentState
                    self.__LastAction = self.__CurrentAction
                    if self.__CurrentAction == 0:
                        FinalDecision = 'C'
                    else:
                        FinalDecision = 'D'
                else:
                    # from the next round, begin Q-Table updating
                    self.__oppLastN.pop(0)
                    self.__mybeforeLastN.pop(0)

                    # state options corresponding to the previous part

                    # self.__CurrentState = tuple(self.__hisbeforeLastN) # SAP

                    self.__CurrentState = (str(self.__mybeforeLastN.count('C')), str(self.__oppLastN.count('C'))) # FSC

                    # self.__CurrentState = (str(self.__mybeforeLastN.count('C')), str(self.__oppLastN.count('C')), int(self.__OppC/self.getRoundsPlayed() * 10)) # SCT+OCP
                    FinalDecision = self.learningResult(OppLast, game)

            return FinalDecision

    def learningResult(self, OppLastAction, game):
        Reward = self.getReward(OppLastAction, game)
        if self.__CurrentState not in SequentialRL.__QTable:
            SequentialRL.__QTable[self.__CurrentState] = [0, 0]

        self.__CurrentAction = self.getBestAction(self.__CurrentState, game)

        sigma = Reward + game.RL_disF * SequentialRL.__QTable[self.__CurrentState][self.__CurrentAction] - \
                SequentialRL.__QTable[self.__LastState][self.__LastAction]


        SequentialRL.__QTable[self.__LastState][self.__LastAction] += game.RL_lR * sigma

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

        return GAME.pd.get((my, OppLast))[0] - 2

    def getBestAction(self, state, game):
        self.__ExplorePercentage = -(5.0 / game.Iter_N) * SequentialRL.__Counter + 5

        if random.randint(0, 99) < self.__ExplorePercentage:
            return random.randint(0, 1)
        else:
            if SequentialRL.__QTable[state][0] >= SequentialRL.__QTable[state][1]:
                return 0
            else:
                return 1


    def name(self):
        return "RL based straegy for the IPD with sequential information"

    def author(self):
        return "******"
