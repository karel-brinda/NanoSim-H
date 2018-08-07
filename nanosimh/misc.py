"""
@copyright 2016 Chen Yang
@copyright 2017 Karel Brinda

Created by Chen Yang <cheny@bcgsc.ca> (NanoSim)
Forked and modified by Karel Brinda <kbrinda@hsph.harvard.edu> (NanoSim-H)

License: GPLv3
"""

import os


def assert_file_exists(fn, test_nonempty=False):
    assert os.path.isfile(fn), "File '{}' does not exist.".format(fn)


def assert_file_nonempty(fn):
    statinfo = os.stat(fn)
    file_size = statinfo.st_size
    assert file_size > 0, "File '{}' is empty".format(fn)
