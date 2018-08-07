"""
@copyright 2016 Chen Yang
@copyright 2017 Karel Brinda

Created by Chen Yang <cheny@bcgsc.ca> (NanoSim)
Forked and modified by Karel Brinda <kbrinda@hsph.harvard.edu> (NanoSim-H)

License: GPLv3
"""

from .simulate import *
from .train import *
from .mixed_models import *

import sys


def nanosimh_simulate():
    simulate.main()


def nanosimh_train():
    train.main()
