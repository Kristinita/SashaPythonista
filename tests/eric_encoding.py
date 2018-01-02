# -*- coding: utf-8 -*-
# @Author: Kristinita
# @Date: 2018-01-02 09:40:46
# @Last Modified time: 2018-01-02 18:39:06
"""Encoding checker.

Check, that files in Windows-1251 encoding.

Bugs:
    1. if no Cyrillic symbols in a file, chardet detect file encoding as ASCII;
    2. chardet can detect Windows-1251 as MacCyrillic.
"""
import chardet
import os

# Do not use «from <module> import *»
# http://bit.ly/2CuW5GS
from eric_config import all_txt_in_eric_room_wihtout_subfolders
from eric_config import log

# Flags, see https://www.computerhope.com/jargon/f/flag.htm
# https://stackoverflow.com/a/48052480/5951529
failure_tests = False

# Get list all filenames in a directory
# https://stackoverflow.com/a/1120736/5951529
for filename in all_txt_in_eric_room_wihtout_subfolders:

    filename_without_path = os.path.basename(filename)

    # Not 100%, see https://stackoverflow.com/a/436299/5951529
    # Can doesn't work for Latin packages
    # Check decoding — http://bit.ly/2C3xSUD
    # https://stackoverflow.com/a/37531241/5951529
    rawdata = open(filename, "rb").read()
    chardet_data = chardet.detect(rawdata)
    # Python dictionary
    fileencoding = (chardet_data['encoding'])
    chardet_confidence = (chardet_data['confidence'])

    # Needs MacCyrillic, because chardet can check Windows-1251
    # as MacCyrillic
    if fileencoding == 'windows-1251':
        log.debug(filename_without_path + " in windows-1251 encoding")
    # Integer to string:
    # https://stackoverflow.com/a/961638/5951529
    elif fileencoding == 'MacCyrillic':
        log.debug(
            filename_without_path +
            " save in MacCyrillic encoding with confidence " +
            str(chardet_confidence))
    else:
        log.critical(
            filename_without_path +
            " save in " +
            fileencoding +
            ", not in windows-1251 encoding. Please, save a file in windows-1251.")
        failure_tests = True

if failure_tests:
    exit(1)

if not failure_tests:
    log.notice("All files in Windows-1251 encoding")
