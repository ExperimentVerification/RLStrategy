#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Game settings
import random
class Games(object):
    # game setting for the RL methods
    RL_lR = 0.1
    RL_disF = 0.9
    RL_memLen = 4
    # iteration number
    Iter_N = 200

    # payoff matrix of the games
    pd = {('C', 'C'): (3, 3),
          ('C', 'D'): (0, 5),
          ('D', 'C'): (5, 0),
          ('D', 'D'): (1, 1)}
    # optional types of games with different payoff values
    # pd = {('C', 'C'): (8, 8),
    #       ('C', 'D'): (0, 10),
    #       ('D', 'C'): (10, 0),
    #       ('D', 'D'): (3, 3)}
    # pd = {('C', 'C'): (4, 3),
    #       ('C', 'D'): (4, 2),
    #       ('D', 'C'): (2, 3),
    #       ('D', 'D'): (2, 2)}
    # pd = {('C', 'C'): (random.randint(0,10), random.randint(0,10)),
    #       ('C', 'D'): (random.randint(0,10), random.randint(0,10)),
    #       ('D', 'C'): (random.randint(0,10), random.randint(0,10)),
    #       ('D', 'D'): (random.randint(0,10), random.randint(0,10))}

    # for parameter investigation
    def __init__(self, lR = None, disF = None, gameLen = None, memLen = None):
        if lR:
            Games.RL_lR = lR

        if disF:
            Games.RL_disF = disF

        if gameLen:
            Games.Iter_N = gameLen

        if memLen:
            Games.RL_memLen = memLen

        print 'lr', Games.RL_lR
        print 'disF', Games.RL_disF
        print 'gameLen', Games.Iter_N
        print 'memoryLen', Games.RL_memLen