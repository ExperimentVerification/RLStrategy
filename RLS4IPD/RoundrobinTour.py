#!/usr/bin/env python
# -*- coding: utf-8 -*-

# round-robin tournament for the IPD strategies
from Strategy import *
from Score import *
from Games import *
from IteratedPD import *
import numpy
from ALLC import *
from ALLD import *
from TFT import *
from Grim import *
from SM import *
from HM import *
from perDDC import *
from perCCD import *
from STFT import *
from perCD import *
from Pavlov import *
from TFTT import *
from hard_tft import *
from slow_tft import *
from Gradual import *
from Prober import *
from mem2 import *
from spiteful_cc import *
from winner12 import *
from winner21 import *
from tft_spiteful import *
from SequentialRL import *
from ParallelRL import *
from SingleState import *
from RAND import *

from cCCCCspite import *
from cDCCCspite import *
from dCCCCspite import *
from dDCCCspite import *

from cCCCDspite import *
from cDCCDspite import *
from dCCCDspite import *
from dDCCDspite import *

from cCCDCspite import *
from cDCDCspite import *
from dCCDCspite import *
from dDCDCspite import *

from cCCDDspite import *
from cDCDDspite import *
from dCCDDspite import *
from dDCDDspite import *

from cCDCCspite import *
from cDDCCspite import *
from dCDCCspite import *
from dDDCCspite import *

from cCDCDspite import *
from cDDCDspite import *
from dCDCDspite import *
from dDDCDspite import *

from cCDDCspite import *
from cDDDCspite import *
from dCDDCspite import *
from dDDDCspite import *

from cCDDDspite import *
from cDDDDspite import *
from dCDDDspite import *
from dDDDDspite import *


lst = [ALLC,        # 0
       ALLD,        # 1
       TFT,         # 2
       Grim,        # 3
       SM,          # 4
       HM,          # 5
       perDDC,      # 6
       perCCD,      # 7
       STFT,        # 8
       perCD,       # 9
       Pavlov,      # 10
       TFTT,        # 11
       hard_tft,    # 12
       slow_tft,    # 13
       Gradual,     # 14
       Prober,      # 15
       mem2,        # 16
       spiteful_cc, # 17
       winner12,    # 18
       winner21,    # 19
       tft_spiteful,# 20
       SequentialRL,# 21
       # ParallelRL,
       # SingleState
       # RAND,
       # cCCCCspite,
       # cDCCCspite,
       # dCCCCspite,
       # dDCCCspite,
       # cCCCDspite,
       # cDCCDspite,
       # dCCCDspite,
       # dDCCDspite,
       # cCCDCspite,
       # cDCDCspite,
       # dCCDCspite,
       # dDCDCspite,
       # cCCDDspite,
       # cDCDDspite,
       dCCDDspite,  # winning - 22
       dDCDDspite,  # winning - 23
       # cCDCCspite,
       # cDDCCspite,
       # dCDCCspite,
       # dDDCCspite,
       # cCDCDspite,
       # cDDCDspite,
       # dCDCDspite,
       # dDDCDspite,
       # cCDDCspite,
       # cDDDCspite,
       # dCDDCspite,
       # dDDDCspite,
       # cCDDDspite,
       # cDDDDspite,
       dCDDDspite,  # winning - 24
       dDDDDspite   # winning - 25
       ]


results = {}
OverallScore = {} # for getting average performance in several round-robin tournaments
payoff = {}
# one round tournament
def RoundrobinTour(lst, gameHere):
    score = {}
    for i in range(len(lst)):
        if lst[i] not in score:
            score[lst[i]] = 0.0
        # score.append(float(0))
        for j in range(len(lst)):
            if lst[j] not in score:
                score[lst[j]] = 0.0
            a1 = lst[i](gameHere)
            b1 = lst[j](gameHere)
            [scA, scB] = IteratedPD(a1, b1, gameHere)
            score[lst[i]] += scA
            payoff[(lst[i], lst[j])] = scA
            payoff[(lst[j], lst[i])] = scB
            # score[lst[j]] += scB
    sortedDic = sorted(score.items(), key=lambda score: score[1], reverse=True)
    print sortedDic, 'dic'
    for ele in score:
        if ele not in OverallScore:
            OverallScore[ele] = 0.0
        OverallScore[ele] += score[ele]
    winning = sortedDic[0][0]
    if winning not in results.keys():
        results[winning] =0
    results[winning] += 1


NN = 0
# games(learning rate, discount factor, game length, memory length for the RL agent)
games = Games(None, None, None, None) # game setting choice for parameter investigation
# 50 trials
while(NN < 50):
    # OverallScore = []
    RoundrobinTour(lst, games)
    NN += 1
    print NN
    print results # shows the winning strategy

for eleme in OverallScore:
    OverallScore[eleme] = OverallScore[eleme]/50.0

# print OverallScore
# sortedos = sorted(OverallScore.items(), key=lambda OverallScore: OverallScore[1], reverse=True)
# print sortedos

# sortedRes = sorted(results.items(), key=lambda results: results[1], reverse=True)
# wp = float(results[sortedRes[0][0]])/float(10)

# file writing for experiments
# f.write(str(sortedRes[0][0]) + 'GameLen = 1500: ' + str(wp))
# f.write(str(sortedRes) + '  : ' + str(wp))
# f = open('TEST.txt','a')
# f.write(OverallScore)
# f.write('\n')
# f.close()