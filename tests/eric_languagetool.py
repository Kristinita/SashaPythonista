# -*- coding: utf-8 -*-
# @Author: Kristinita
# @Date: 2018-01-02 15:30:08
# @Last Modified time: 2018-01-05 14:52:36
"""LanguageTool Python.

LanguageTool wrapper for Python.
"""
from pyfancy import pyfancy

# Do not use «from <module> import *»
# http://bit.ly/2CuW5GS
from eric_config import all_txt_in_eric_room_wihtout_subfolders
from eric_config import log

import language_check
import os

tool_language = language_check.LanguageTool('ru-RU')

# Flags, see https://www.computerhope.com/jargon/f/flag.htm
# https://stackoverflow.com/a/48052480/5951529
languagetool_failure_tests = False

# Get list all filenames in a directory
# https://stackoverflow.com/a/1120736/5951529
for filename in all_txt_in_eric_room_wihtout_subfolders:

    # Filename without path
    # https://stackoverflow.com/a/678266/5951529
    filename_without_path = os.path.basename(filename)

    log.debug(filename_without_path + "\n")
    # Read file content
    # https://stackoverflow.com/a/3758177/5951529
    file_text = open(filename, encoding='windows-1251').read()

    error_list = tool_language.check(file_text)
    # Print all tuples in list values
    # https://stackoverflow.com/a/15769313/5951529
    print(*error_list, sep='\n\n')
    if not error_list:
        log.debug(
            "Not detect errors and typos in" +
            filename_without_path +
            "\n\n")
    else:
        log.warning(pyfancy().red(
            "Detect error(s) or/and typo(s) in " + filename_without_path + "\n\n"))
        languagetool_failure_tests = True

if not languagetool_failure_tests:
    log.notice(pyfancy().green().bold(
        "LanguageTool no detect errors and typos for all files"))

if languagetool_failure_tests:
    log.warning(pyfancy().red(
        "LanguageTool detect error(s) or/and typo(s). Please, review it."))
