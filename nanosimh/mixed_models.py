#!/usr/bin/env python
"""
@copyright 2016 Chen Yang
@copyright 2017 Karel Brinda

Created by Chen Yang <cheny@bcgsc.ca> (NanoSim)
Forked and modified by Karel Brinda <kbrinda@hsph.harvard.edu> (NanoSim-H)

License: GPLv3

This script is used to generate random numbers following certain mixed distribution models
"""

import math
import numpy

# numpy.random.geometric generate positive integers, starting from 1
# the rgeom in R generate values starting from 0


def pois_geom(lam, prob, weight):
    tmp_rand = numpy.random.random()
    if tmp_rand < weight:
        value = numpy.random.poisson(lam) + 1
    else:
        value = numpy.random.geometric(prob)
    return value


def wei_geom(lam, k, prob, weight):
    tmp_rand = numpy.random.random()
    if tmp_rand < weight:
        value = int(round(math.ceil(lam * numpy.random.weibull(k))))
    else:
        value = numpy.random.geometric(prob) - 1

    if value == 0:
        value = 1

    return value
