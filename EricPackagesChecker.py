# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2017-12-31 15:43:57
# @Last Modified time: 2018-01-01 16:18:43
"""Test module for Eric's rooms packages.

Tests for continuous integration EricsRooms packages. EricPackageChecker.py
check for each .txt file,
that:

1. File contains <body> tag.
2. File saved in Windows-1251 encoding.
3. On each line of file «*» symbol.
    3.1. For lines after <body> tag.
    3.2. Not check for <!-- comments --> lines.
"""
import chardet
import glob

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
all_txt_in_eric_room_wihtout_subfolders = glob.glob('*.txt')

# Get list all filenames in a directory
# https://stackoverflow.com/a/1120736/5951529
for filename in all_txt_in_eric_room_wihtout_subfolders:

    # Check if string in a file
    # https://stackoverflow.com/a/4944929/5951529
    if "<body>" in open(filename).read():
        log.debug(filename + " contains <body>")
    else:
        log.error("File " + filename + " not contain <body> . \
            Please, add <body> in " + filename + ".")

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
        log.debug(filename + " in windows-1251 encoding")
    # Integer to string:
    # https://stackoverflow.com/a/961638/5951529
    elif fileencoding == 'MacCyrillic':
        log.debug(
            filename +
            " save in MacCyrillic encoding with confidence " +
            str(chardet_confidence))
    else:
        log.critical(filename + " save in " + fileencoding + ", not in \
           windows 1251 encoding. Please, save a file in windows - 1251.")

    # Lines to list
    # https://stackoverflow.com/a/3277515/5951529
    with open(filename) as filename_as_list:
        submit_file_as_list = filename_as_list.readlines()
        # New list after <body>
        # https://stackoverflow.com/a/35880897/5951529
        get_lines_with_body = submit_file_as_list.index('<body>\n')
        list_without_lines_with_body = submit_file_as_list[get_lines_with_body
                                                           + 1:]
        # Remove list item, contains «<!--»
        # https://stackoverflow.com/a/3416473/5951529
        list_without_lines_with_body_and_comments = [x for x in
                                                     list_without_lines_with_body if '<!--' not in x]
        # Check all elements of list, that contains «*»
        # https://stackoverflow.com/a/44118151/5951529
        # List comprehension: print incorrect list items
        # https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
        if all('*' in item for item in list_without_lines_with_body_and_comments):
            log.debug("All lines in " + filename + " contains asterisks")
        else:
            lines_without_asterisks = [item for item in
                                       list_without_lines_with_body_and_comments if '*' not in
                                       item]
            # Remove \n symbol in end of the lines
            # https://stackoverflow.com/a/30881893/5951529
            lines_without_asterisks_and_n = list(
                map(str.strip, lines_without_asterisks))
            # Lists to strings with quotes
            # https://stackoverflow.com/a/13207725/5951529
            lines_without_asterisks_and_n_as_strings = str(
                lines_without_asterisks_and_n)[1:-1]
            log.error("This line(s) not contains asterisks: " +
                      lines_without_asterisks_and_n_as_strings + " in " + filename)
