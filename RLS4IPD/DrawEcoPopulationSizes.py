#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import random
from itertools import cycle
from cycler import cycler

# for ecological performance illustrating
def DrawEcoPopulationSizes(populationSizes, lst):
    evolution = []
    for iplayer in range(len(lst)):
        evolution.append([])
    print evolution
    print len(populationSizes)
    print len(evolution)
    for iturn in range(len(populationSizes)):
        for ip in range(len(evolution)):
            evolution[ip].append(populationSizes[iturn][ip] * 100 * len(lst))
    turns = range(len(populationSizes))

    # plot
    fig = plt.figure()
    ax = plt.subplot()
    lines = ['solid', 'dashed', 'dashdot', 'dotted']
    colours = ['grey', 'darksalmon', 'c', 'magenta', 'hotpink', 'maroon',
               'y', 'teal', 'cyan', 'chocolate', 'gold', 'peru',
               'orange', 'dodgerblue', 'thistle', 'crimson', 'darkviolet', 'navy',
               'b', 'deepskyblue', 'yellow', 'aqua']
    plt.gca().set_color_cycle(colours)
    for iplot in range(len(evolution)):
        # style = random.randint(0, 3)
        style = iplot % 4
        ax.plot(turns, evolution[iplot],
                # label= lst[iplot],
                label = iplot,
                linestyle = lines[style]
                # color = colours[iplot]
                )
    plt.legend(loc='upper left', ncol=1, bbox_to_anchor=(1, 1.05),
               # prop=fontP,
               prop={'size': 10},
               fancybox=True, shadow=False
               # title='LEGEND'
               )
    plt.ylim([0, 300])
    plt.xlabel("generation", fontsize=20)
    plt.ylabel("population", fontsize=20)
    # plt.show()
    return plt
