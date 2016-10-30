#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ecological tournament for the IPD
import time, datetime, os
from Strategy import *
from Score import *
from Games import *
from IteratedPD import *
from EcoSystem import *
from DrawEcoPopulationSizes import *
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

lst = [ALLC,            # 0
       ALLD,            # 1
       TFT,             # 2
       Grim,            # 3
       SM,              # 4
       HM,              # 5
       perDDC,          # 6
       perCCD,          # 7
       STFT,            # 8
       perCD,           # 9
       Pavlov,          # 10
       TFTT,            # 11
       hard_tft,        # 12
       slow_tft,        # 13
       Gradual,         # 14
       Prober,          # 15
       mem2,            # 16
       spiteful_cc,     # 17
       winner12,        # 18
       winner21,        # 19
       tft_spiteful,    # 10
       SequentialRL,    # 21
       # ParallelRL,
       # SingleState,
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
       # dCCDDspite, # winning - 22
       # dDCDDspite, # winning - 23
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
       # dCDDDspite, # winning - 24
       # dDDDDspite  # winning - 25
       ]



games = Games(None, None, None, None)
# one generation
def getPayoffMatrix(lst, gameHere):
    payoffs = [[0.0 for j in range(len(lst))] for i in range(len(lst))]
    for i in range(len(lst)):
        for j in range(len(lst)):
            a1 = lst[i](gameHere)
            b1 = lst[j](gameHere)
            [scA, scB] = IteratedPD(a1, b1, gameHere)
            payoffs[i][j] = scA/gameHere.Iter_N
            # payoffs[j][i] = scB/gameHere.Iter_N
    return payoffs


# Create new directory to save the figures
now = datetime.datetime.now()
newDirName = now.strftime("%Y_%m_%d-%H%M")
print "Making directory " + newDirName
# os.mkdir(newDirName)


NN = 0
while (NN < 10):
    payoffs = getPayoffMatrix(lst, games)
    print 'payoffs', payoffs
    eco = EcoSystem(payoffs)
    eco.reproduce(35) # generation setting
    print 'pop', eco.populationSize
    p = DrawEcoPopulationSizes(eco.populationSize, lst)
    p.show()
    # p.savefig('{}/graph{NN}.png'.format(newDirName, NN=NN))
    NN += 1
    print NN
