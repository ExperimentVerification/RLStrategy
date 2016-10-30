#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *
from Score import *
from Games import *

# Definition of one complete iterated prisoner's dilemma
def IteratedPD(strategy, opponent, games):
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

        sc.materialScore = strategy.getMaterialSc()
        sc1.materialScore = opponent.getMaterialSc()

    return sc.materialScore, sc1.materialScore