#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc

# lambda - the social coefficient
# has six discrete value of 0.0, 0.2, 0.4, 0.6, 0.8, 1.0
# increase and decrease by one unit of 0.2
class BaseLambda(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, minimum, maximum, increment, startValue):
        self.__minimum = float(minimum)
        self.__maximum = float(maximum)
        self.__increment = float(increment)
        self.__value = self.__fixToDiscrete(startValue, minimum, maximum, increment)
        self.__history = []
        self.__history.append(self.__value)

    def getHistory(self):
        lst = self.__history
        return lst


    def getValue(self):
        return self.__value


    def incrementValue(self):
        self.__value = self.__fixToDiscrete(self.__value + self.__increment, self.__value, self.__value + self.__increment, self.__increment)

        self.__history.append(self.__value)

    def decrementValue(self):
        self.__value = self.__fixToDiscrete(self.__value - self.__increment, self.__value - self.__increment, self.__value, self.__increment)

        self.__history.append(self.__value)

    def nochange(self):
        self.__history.append(self.__value)

    # function to fix the input to the closer of min and max
    def __fixToDiscrete(self, inp, minima, maxima, step):
        outp = 0.0
        # first cap the value
        inp = self.__fixToRange(inp, max(self.__minimum, minima), min(maxima, self.__maximum))
        # for loop with float
        for i in range(5):
            currentMin = minima + i * step
            currentMax = minima + i * step + step

            if inp >= currentMin and inp <= currentMax:
                if inp == currentMin:
                    outp = currentMin
                elif inp == currentMax:
                    outp = currentMax
                elif inp > ((currentMax + currentMin)/2.0):
                    outp = currentMax
                else:
                    outp = currentMin
        return outp


    @staticmethod
    def __fixToRange(inp, minimum, maximum):
        if inp > maximum:
            return maximum
        elif inp < minimum:
            return minimum
        else:
            return inp
