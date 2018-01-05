# -*- coding: utf-8 -*-
# @Author: Kristinita
# @Date: 2018-01-02 08:35:59
# @Last Modified time: 2018-01-04 20:12:49
"""Configuration Erichek file.

Imports and variables for tests.
"""
import glob


# logbook — custom logging:
# http://logbook.readthedocs.io/en/stable/quickstart.html
# Set NOTICE level:
# https://github.com/search?q=StreamHandler(sys.stdout).push_application()&type=Code
import logbook

import sys


logbook.StreamHandler(sys.stdout,
                      level=logbook.NOTICE).push_application()
log = logbook.Logger("Sasha Logbook")

# Get all .txt file in a directory
# https://stackoverflow.com/a/3964689/5951529
all_txt_in_eric_room_wihtout_subfolders = glob.glob('./*.txt')
