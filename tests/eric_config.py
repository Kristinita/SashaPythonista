# -*- coding: utf-8 -*-
# @Author: Kristinita
# @Date: 2018-01-02 08:35:59
# @Last Modified time: 2018-01-02 09:39:40
"""Configuration file.

Imports and variables.
"""
import glob
import os

# logbook — custom logging:
# http://logbook.readthedocs.io/en/stable/quickstart.html
# Set INFO level:
# https://github.com/search?q=StreamHandler(sys.stdout).push_application()&type=Code
import logbook

import sys
logbook.StreamHandler(sys.stdout,
                      level=logbook.NOTICE).push_application()
log = logbook.Logger("Sasha Logbook")

# Get all .txt file in a directory
# https://stackoverflow.com/a/3964689/5951529
all_txt_in_eric_room_wihtout_subfolders = glob.glob('./*.txt')

# Filename without path
# https://stackoverflow.com/a/678266/5951529
for filename in all_txt_in_eric_room_wihtout_subfolders:

    filename_without_path = os.path.basename(filename)
