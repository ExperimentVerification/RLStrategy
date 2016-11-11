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
    
    # Prisoner's Dilemma - 2
    # pd = {('C', 'C'): (7, 7),
    #       ('C', 'D'): (3, 8),
    #       ('D', 'C'): (8, 3),
    #       ('D', 'D'): (0, 0)}
    
    # The Battle of the Sexes - 1
    # pd = {('C', 'C'): (10, 5),
    #       ('C', 'D'): (0, 0),
    #       ('D', 'C'): (0, 0),
    #       ('D', 'D'): (5, 10)}
    
    # The Battle of the Sexes - 2
    # pd = {('C', 'C'): (3, 2),
    #       ('C', 'D'): (0, 0),
    #       ('D', 'C'): (0, 0),
    #       ('D', 'D'): (2, 3)}
    
    # The Game of Chicken - 1
    # pd = {('C', 'C'): (3, 3),
    #       ('C', 'D'): (1, 4),
    #       ('D', 'C'): (4, 1),
    #       ('D', 'D'): (0, 0)}
    
    # The Game of Chicken - 2
    # pd = {('C', 'C'): (4, 4),
    #       ('C', 'D'): (1, 7),
    #       ('D', 'C'): (7, 1),
    #       ('D', 'D'): (0, 0)}

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
