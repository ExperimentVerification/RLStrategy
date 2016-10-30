#!/usr/bin/env python
# -*- coding: utf-8 -*-

# the round-robin tournament for the iterated Double-Game Prisoner's Dilemma
from Strategy import *
from Score import *
from Games import *
from BoydABitNicer import *
from BoydABitRandom import *
from BoydAEGS import *
from BoydAEGSS import *
from BoydAlwaysCooperate import *
from BoydAlwaysDefects import *
from BoydAlwaysRandom import *
from BoydBayesian import *
from BoydBayesianTitForTat import *
from BoydDoubleIncrement import *
from BoydEightyPercentNice import *
from BoydExtendedTitForTat import *
from BoydNashDefect import *
from BoydNashTitForTat import *
from BoydNegativePeople import *
from BoydNonsensePeople import *
from BoydPositivePeople import *
from BoydRafalStrategy import *
from BoydRandomTitForTat import *
from BoydRLQTableI import *
from BoydRLQTableIPlus import *
from BoydSocialTitForTat import *
from BoydTitForTat import *
from twoStageRLbased import *
from IteratedMGame import *
from RLABitRandom import *
from RLAEGS import *
from RLAlwaysCooperate import *
from RLAlwaysDefects import *
from RLAlwaysRandom import *
from RLRandomTitForTat import *
from RLTitForTat import *

lst = [ BoydABitNicer,
        BoydABitRandom,
        BoydAEGS,
        BoydAEGSS,
        BoydAlwaysCooperate,
        BoydAlwaysDefects,
        BoydAlwaysRandom,
        BoydBayesian,
        BoydBayesianTitForTat,
        BoydDoubleIncrement,
        BoydEightyPercentNice,
        BoydExtendedTitForTat,
        BoydNashDefect,
        BoydNashTitForTat,
        BoydNegativePeople,
        BoydNonsensePeople,
        BoydPositivePeople,
        BoydRafalStrategy,
        BoydRandomTitForTat,
        BoydRLQTableI,
        # BoydRLQTableIPlus,
        BoydSocialTitForTat,
        BoydTitForTat,
        # RLABitRandom,
        # RLAEGS,
        # RLAlwaysCooperate,
        # RLAlwaysDefects,
        # RLAlwaysRandom,
        # RLRandomTitForTat,
        # RLTitForTat,
        twoStageRLbased
        ]

results = {}
mresults = {}
sresults = {}
games = Games()

# tournament 1 - mvspt
def TournaMent(lst, gameHere):
    score = {} # for overall score
    mscore = {} # for material score
    sscore = {} # for social score
    for i in range(len(lst)):
        if lst[i] not in score:
            score[lst[i]] = 0
        if lst[i] not in mscore:
            mscore[lst[i]] = 0
        if lst[i] not in sscore:
            sscore[lst[i]] = 0
        # score.append(float(0))
        for j in range(len(lst)):
            if lst[j] not in score:
                score[lst[j]] = 0
            if lst[j] not in mscore:
                mscore[lst[j]] = 0
            if lst[j] not in sscore:
                sscore[lst[j]] = 0
            a1 = lst[i](gameHere)
            b1 = lst[j](gameHere)
            [msc, ssc, agsc, agscb] = IteratedMGame(a1, b1, gameHere)
            mscore[lst[i]] += msc
            sscore[lst[i]] += ssc
            score[lst[i]] += agsc
            # score[lst[j]] += agscb
    sortedDic = sorted(score.items(), key=lambda score: score[1], reverse=True)
    sortedmDic = sorted(mscore.items(), key=lambda mscore: mscore[1], reverse=True)
    sortedsDic = sorted(sscore.items(), key=lambda sscore: sscore[1], reverse=True)
    print 'DIC',sortedDic
    print 'MDIC', sortedmDic
    print 'SDIC', sortedsDic
    # The overall winner must have both positive material and social scores
    for iall in range(len(lst)):
        str = sortedDic[iall][0]
        for jall in range(len(lst)):
            if sortedsDic[jall][0] == str:
                break
        if sortedsDic[jall][1] != 0 and sortedmDic[jall][1] != 0:
            winning = str
            break

    # winning = sortedDic[0][0]
    # The winner of the material game must hava a positive social score, to make sure that it is not antisocail
    # the material game winner must participate in the social game
    for i in range(len(lst)):
        str = sortedmDic[i][0]
        # print 'stri', str
        for j in range(len(lst)):
            if sortedsDic[j][0] == str:
                break
        if sortedsDic[j][1] != 0:
            mwinning = str
            break
    # The winner of the social game must have a positive material score
    # the social game winner must participate in the material game
    for ii in range(len(lst)):
        str = sortedsDic[ii][0]
        for jj in range(len(lst)):
            if sortedmDic[jj][0] == str:
                break
        if sortedmDic[jj][1] != 0:
            swinning = str
            break
    # swinning = sortedsDic[0][0]
    # winning = lst[score.index(max(score))]
    if winning not in results.keys():
        results[winning] =0
    results[winning] += 1

    if mwinning not in mresults.keys():
        mresults[mwinning] = 0
    mresults[mwinning] += 1

    if swinning not in sresults.keys():
        sresults[swinning] = 0
    sresults[swinning] += 1



NN = 0
while (NN < 500):
    TournaMent(lst, games)
    NN += 1
    print NN
    print 'Overall', results
    print 'Material', mresults
    print 'Social', sresults