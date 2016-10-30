#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
# game settings
class Games(object):
    noGame = 0
    Games = []
    # game setting for the RL methods
    RL_Poc = 0.3
    RL_lR = 0.1
    RL_disF = 0.9
    RL_memLen = 4

    RL_ccLambdaA = 3
    RL_ccLambdaB = 2.5
    RL_cdLambda = 2.5
    RL_dcLambda = 5
    RL_ddLambda = 1

    # default constants - lambda
    Lambda_min = 0.0
    Lambda_max = 1.0
    Lambda_incr = 0.2
    Lambda_global = 0.5
    Iter_N = 200


    # payoff matrix of the games
    # Double-game Prisoner's Dilemma
    game1 = {('C', 'C'): (3, 3),
             ('C', 'D'): (0, 5),
             ('D', 'C'): (5, 0),
             ('D', 'D'): (1, 1)}
    game2 = {('C', 'C'): (2.5, 2.5),
             ('C', 'D'): (2.5, 0),
             ('D', 'C'): (0, 2.5),
             ('D', 'D'): (0, 0)}


    def __init__(self):
        self.Games.append(Games.game1)
        self.Games.append(Games.game2)
        self.noGame = len(self.Games)