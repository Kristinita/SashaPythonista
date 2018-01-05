# -*- coding: utf-8 -*-
# @Author: Kristinita
# @Date: 2018-01-02 08:22:06
# @Last Modified time: 2018-01-05 17:42:45
"""Body Checker.

Check, that <body> contains in files.
"""
import os

from eric_config import clize_log_level
from pyfancy import pyfancy
# Do not use «from <module> import *»
# http://bit.ly/2CuW5GS
from eric_config import all_txt_in_eric_room_wihtout_subfolders
from eric_config import log

# Flags, see https://www.computerhope.com/jargon/f/flag.htm
# https://stackoverflow.com/a/48052480/5951529
body_failure_tests = False

clize_log_level()

# Get list all filenames in a directory
# https://stackoverflow.com/a/1120736/5951529
for filename in all_txt_in_eric_room_wihtout_subfolders:

    filename_without_path = os.path.basename(filename)

    # Check if string in a file
    # https://stackoverflow.com/a/4944929/5951529
    # Encoding for Travis CI, see
    # https://stackoverflow.com/a/31492722/5951529
    # https://github.com/travis-ci/travis-ci/issues/8993#issuecomment-354674238
    # https://github.com/travis-ci/travis-ci/issues/8993#issuecomment-354681085
    if "<body>" in open(filename, encoding='windows-1251').read():
        log.debug(filename_without_path + " contains <body>")
    else:
        log.error(pyfancy().red().bold(
            "File " +
            filename_without_path +
            " not contain <body>. Please, add <body> in " +
            filename_without_path +
            "."))
        body_failure_tests = True

if body_failure_tests:
    log.error(pyfancy().red().bold(
        "Not all files contains <body>. Please, correct it."))

if not body_failure_tests:
    log.notice(pyfancy().green().bold("All files contains <body>"))
