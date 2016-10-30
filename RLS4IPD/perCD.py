#!/usr/bin/env python
# -*- coding: utf-8 -*-

# per_cd, plays cd periodically
# CDCDCDCDCD.......
from Strategy import *

class perCD(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self.count = 0

    def respond(self, game):
        if self.count == 0:
            self.count += 1
            return 'C'
        else:
            self.count = 0
            return 'D'

    def name(self):
        return "Per CD"

    def author(self):
        return "******"