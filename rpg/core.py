# SPDX-FileCopyrightText: 2022 Daniel S. Haag
#
# SPDX-License-Identifier: MIT

# -*- coding: utf-8 -*-
from . import rules

import numpy as np

def roll():
    return np.random.randint(1, high=rules.diceHigh(), size=rules.diceNum(), dtype='l')
