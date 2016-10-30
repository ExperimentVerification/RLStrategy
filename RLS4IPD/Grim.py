#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Grim trigger(Grim): Cooperates, until the opponent defects, and thereafter always defects.
# also called spiteful
from Strategy import *

class Grim(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self.defected = False

    def respond(self, game):
        if self.getLastResponsePair() == 0:
            return 'C'
        else:
            if self.getLastResponsePair()[1] == 'D':
                self.defected = True

            if self.defected == True:
                return 'D'

            return 'C'

    def name(self):
        return "Grim trigger"

    def author(self):
        return "******"