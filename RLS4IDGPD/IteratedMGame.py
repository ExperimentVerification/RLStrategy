#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *
from Score import *



# Definition of one complete iterated DGPD
def IteratedMGame(strategy, opponent, games):
    strategy.setOpponent(opponent)
    opponent.setOpponent(strategy)

    sc = Score(strategy.name(), strategy.author(), opponent.name())   # get the scores
    sc1 = Score(opponent.name(), opponent.author(), strategy.name())

    while(sc.runsMade < games.Iter_N):
        strategy.play(games)    # play one round
        opponent.play(games)

        strategy.calculateScore(games)
        opponent.calculateScore(games)
        sc.runsMade += 1
        sc1.runsMade += 1

        sc.lambd = strategy.getLastLambda()
        sc.materialScore = strategy.getMaterialSc()
        sc.socialScore = strategy.getSocialSc()
        sc.aggregates = sc.socialScore * games.Lambda_global + sc.materialScore * (1.0 - games.Lambda_global)

        sc1.lambd = opponent.getLastLambda()
        sc1.materialScore = opponent.getMaterialSc()
        sc1.socialScore = opponent.getSocialSc()
        sc1.aggregates = sc1.socialScore * games.Lambda_global + sc1.materialScore * (1.0 - games.Lambda_global)

    return sc.materialScore, sc.socialScore, sc.aggregates, sc1.aggregates