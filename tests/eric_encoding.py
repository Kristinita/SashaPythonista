# -*- coding: utf-8 -*-
# @Author: Kristinita
# @Date: 2018-01-02 09:40:46
# @Last Modified time: 2018-01-04 17:05:40
"""Encoding checker.

Check, that files in Windows-1251 encoding.

Bugs:
    1. if no Cyrillic symbols in a file, chardet detect file encoding as ASCII;
    2. chardet can detect Windows-1251 as MacCyrillic.
"""
import chardet
import codecs
import os

# Do not use «from <module> import *»
# http://bit.ly/2CuW5GS
from eric_config import all_txt_in_eric_room_wihtout_subfolders
from eric_config import log


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
        log.notice(
            "Encoding of file " + filename_without_path +
            " chardet detect as MacCyrillic with confidence " +
            str(chardet_confidence))
    else:
        # Convert file from UTF-8 to Cyrillic 1251
        # https://stackoverflow.com/q/19932116/5951529
        with codecs.open(filename, "r", "utf-8") as file_for_conversion:
            read_file_for_conversion = file_for_conversion.read()
        with codecs.open(filename, "w", "windows-1251") as file_for_conversion:
            if read_file_for_conversion:
                file_for_conversion.write(read_file_for_conversion)
        log.notice(
            filename_without_path +
            " converted from UTF-8 to Windows-1251")


log.notice("All files in Windows-1251 encoding")
