#!/usr/bin/env python
# -*- coding: utf-8 -*-
from numpy import std
import random
import matplotlib
import matplotlib.pyplot
import matplotlib.transforms

# ecosystem for reproducing
class EcoSystem(object):

    def __init__(self, payoff_matrix, fitness = None, population = None):
        self.payoffMatrix = payoff_matrix
        self.payoffStddev = self.getPayoffStddevs(payoff_matrix)

        if population:
            if min(population) < 0:
                raise TypeError('Non-negative population not satisfied.')
            elif len(population) != len(payoff_matrix):
                raise TypeError('Population length wrong!')
            else:
                norm = float(sum(population))
                self.populationSize = [[p / norm for p in population]]
        else:
            self.populationSize = [[1.0 / len(payoff_matrix) for i in range(len(payoff_matrix))]]

        if fitness:
            self.fitness = fitness
        else:
            self.fitness = lambda p: p

    def getPayoffStddevs(self, payoff_matrix):
        plist = list(range(len(payoff_matrix)))
        payoff_stddevs = [[[0] for opponent in plist] for player in plist]

        for player in plist:
            for opponent in plist:
                utilities = payoff_matrix[player][opponent]

                if utilities:
                    payoff_stddevs[player][opponent] = std(utilities)
                else:
                    payoff_stddevs[player][opponent] = 0

        return payoff_stddevs



    def reproduce(self, turns):

        for iturn in range(turns):

            plist = list(range(len(self.payoffMatrix)))
            pops = self.populationSize[-1]

            payoffs = [0 for ip in plist]
            for ip in plist:
                for jp in plist:
                    avg = self.payoffMatrix[ip][jp]
                    dev = self.payoffStddev[ip][jp]
                    p = random.normalvariate(avg, dev)
                    payoffs[ip] += p * pops[jp]

            fitness = [self.fitness(p) for p in payoffs]
            newpops = [p * f for p, f in zip(pops, fitness)]

            norm = sum(newpops)
            newpops = [p / norm for p in newpops]

            self.populationSize.append(newpops)