#!/usr/bin/env python
# -*- coding: utf-8 -*-

# per_ddc, plays ddc periodically
# DDCDDCDDCDDCDDCDDC......
from Strategy import *

class perDDC(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self.count = 0

    def respond(self, game):
        if self.count == 0:
            self.count += 1
            return 'D'
        elif self.count == 1:
            self.count += 1
            return 'D'
        else:
            self.count = 0
            return 'C'

    def name(self):
        return "Per DDC"

    def author(self):
        return "******"