"""
Created by Chen Yang <cheny@bcgsc.ca>
Modified by Karel Brinda <kbrinda@hsph.harvard.edu>

License: GPL
"""

from .simulate import *
from .train import *
from .mixed_models import *

import sys

def nanosimh_simulate():
	simulate.main()

def nanosimh_train():
	train.main()
