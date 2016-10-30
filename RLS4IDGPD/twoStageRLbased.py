#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *

# the double-stage RL-based approach
# QTable for lambda:
# S1 - the sequential cooperation times
# S1 - increase, decrease, nochange
# QTable for decision making:
# S2 - the updated lambda
# A2 - C and D
class twoStageRLbased(Strategy):
    __QTable = {}
    __QTable4L = {}
    __Counter = 0
    __LastLambda = 0.0
    __CoopRatio = 0.3

    def __init__(self, game):
        Strategy.__init__(self)
        # decision making parameters
        self.__LastState = -999
        self.__LastAction = -999
        self.__CurrentState = -999
        self.__CurrentAction = -999

        # parameter updating
        self.__LastState4L = -999
        self.__LastAction4L = -999
        self.__CurrentState4L = -999
        self.__CurrentAction4L = -999

        self.__ExplorePercentage = 5.0
        self._lambda = Lambda(twoStageRLbased.__CoopRatio)


        # state constructing parameters
        self.__mybeforeLastN = []
        self.__oppLastN = []
        self.__mybeforeLast = []
        self.__OppC = 0

        twoStageRLbased.__LastLambda = twoStageRLbased.__CoopRatio
        twoStageRLbased.__Counter = 0


    def respond(self, game):
        twoStageRLbased.__Counter += 1
        if self.getLastResponsePair() == 0:
            # cooperate for the first round'
            self._lambda.nochange()
            self.__LastAction4L = 0
            self.__LastAction = 0
            twoStageRLbased.__LastLambda = round(self._lambda.getValue(), 1)
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

            if len(self.__mybeforeLastN) < game.RL_memLen: # memory length
                # play TFT before the first state formed
                self._lambda.nochange()
                return OppLast
            else:
                if self.__LastState == -999:
                    # the seventh round, construct the first state
                    self.__oppLastN.pop(0)


                    self.__CurrentState4L = (str(self.__mybeforeLastN.count('C')), str(self.__oppLastN.count('C')))
                    if self.__CurrentState4L not in twoStageRLbased.__QTable4L:
                        twoStageRLbased.__QTable4L[self.__CurrentState4L] = [0, 0, 0]

                    self.__CurrentAction4L = self.getBestChange(self.__CurrentState4L, game)
                    self.__LastState4L = self.__CurrentState4L
                    self.__LastAction4L = self.__CurrentAction4L
                    self.updateLambda(self.__CurrentAction4L)


                    self.__CurrentState = round(self._lambda.getValue(), 1)
                    if self.__CurrentState not in twoStageRLbased.__QTable:
                        twoStageRLbased.__QTable[self.__CurrentState] = [0, 0]

                    self.__CurrentAction = self.getBestAction(self.__CurrentState, game)
                    self.__LastState = self.__CurrentState
                    self.__LastAction = self.__CurrentAction
                    if self.__CurrentAction == 0:
                        return 'C'
                    else:
                        return 'D'
                else:
                    # from the 8th round, begin Q-Table updating
                    self.__oppLastN.pop(0)
                    self.__mybeforeLastN.pop(0)


                    self.__CurrentState4L = (str(self.__mybeforeLastN.count('C')), str(self.__oppLastN.count('C')))
                    self.learningResult4L(OppLast, game)


                    self.__CurrentState = round(self._lambda.getValue(), 1)

                    FinalDecision = self.learningResult(OppLast, game)

            twoStageRLbased.__LastLambda = round(self._lambda.getValue(), 1)
            return FinalDecision

    def learningResult(self, OppLastAction, game):
        Reward = self.getReward(OppLastAction, game)
        if self.__CurrentState not in twoStageRLbased.__QTable:
            twoStageRLbased.__QTable[self.__CurrentState] = [0, 0]

        self.__CurrentAction = self.getBestAction(self.__CurrentState, game)

        twoStageRLbased.__QTable[self.__LastState][self.__LastAction] += game.RL_lR * (Reward + game.RL_disF * twoStageRLbased.__QTable[self.__CurrentState][self.__CurrentAction] - twoStageRLbased.__QTable[self.__LastState][self.__LastAction])

        self.__LastState = self.__CurrentState
        self.__LastAction = self.__CurrentAction

        if self.__CurrentAction == 0:
            return 'C'
        else:
            return 'D'

    def learningResult4L(self, OppLastAction, game):
        Reward4L = self.getReward(OppLastAction, game)
        if self.__CurrentState4L not in twoStageRLbased.__QTable4L:
            twoStageRLbased.__QTable4L[self.__CurrentState4L] = [0, 0, 0]

        self.__CurrentAction4L = self.getBestChange(self.__CurrentState4L, game)

        twoStageRLbased.__QTable4L[self.__LastState4L][self.__LastAction4L] += game.RL_lR * (Reward4L +
                                                                                    game.RL_disF * twoStageRLbased.__QTable4L[self.__CurrentState4L][self.__CurrentAction4L] -
                                                                                    twoStageRLbased.__QTable4L[self.__LastState4L][self.__LastAction4L])

        self.__LastState4L = self.__CurrentState4L
        self.__LastAction4L = self.__CurrentAction4L

        self.updateLambda(self.__CurrentAction4L)

    def getReward(self, OppLast, GAME):
        valLambda = float(twoStageRLbased.__LastLambda)
        if self.__LastAction == 0:
            my = 'C'
        else:
            my = 'D'

        return (GAME.Games[0].get((my, OppLast))[0] * (1.0 - valLambda) + GAME.Games[1].get((my, OppLast))[0] * valLambda) - 3

    def getBestAction(self, state, game):
        self.__ExplorePercentage = -(5.0 / game.Iter_N) * twoStageRLbased.__Counter + 5

        if random.randint(0, 99) < self.__ExplorePercentage:
            return random.randint(0, 1)
        else:
            return twoStageRLbased.__QTable[state].index(max(twoStageRLbased.__QTable[state]))




    def getBestChange(self, state, game):
        self.__ExplorePercentage = -(5.0 / game.Iter_N) * twoStageRLbased.__Counter + 5

        if random.randint(0, 99) < self.__ExplorePercentage:
            return random.randint(0, 2)
        else:
            return twoStageRLbased.__QTable4L[state].index(max(twoStageRLbased.__QTable4L[state]))


    def updateLambda(self, actionNumber):
        if actionNumber == 0:
            self._lambda.nochange()
        elif actionNumber == 1:
            self._lambda.decrementValue()
        else:
            self._lambda.incrementValue()

    def name(self):
        return "Double-stage RL-based strategy for the iterated DGPD"

    def author(self):
        return "******"