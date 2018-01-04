# -*- coding: utf-8 -*-
# @Author: Kristinita
# @Date: 2018-01-02 09:40:46
# @Last Modified time: 2018-01-04 09:20:53
"""Asterisks Checker.

Check, if astresks contains in each line of package for Eric room.

Do not check:
    1. lines before <body> and line with <body>,
    2. <!-- comments -->.
"""
import os
# Do not use «from <module> import *»
# http://bit.ly/2CuW5GS
from eric_config import all_txt_in_eric_room_wihtout_subfolders
from eric_config import log

# Flags, see https://www.computerhope.com/jargon/f/flag.htm
# https://stackoverflow.com/a/48052480/5951529
asterisks_failure_tests = False

# Get list all filenames in a directory
# https://stackoverflow.com/a/1120736/5951529
for filename in all_txt_in_eric_room_wihtout_subfolders:

    filename_without_path = os.path.basename(filename)

    # Lines to list
    # https://stackoverflow.com/a/3277515/5951529
    with open(filename, encoding='windows-1251') as filename_as_list:
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
            log.debug(
                "All lines in " +
                filename_without_path +
                " contains asterisks")
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
                      lines_without_asterisks_and_n_as_strings +
                      " in " +
                      filename_without_path)
            asterisks_failure_tests = True

if asterisks_failure_tests:
    log.error(
        "One or more your files not contained asterisks. Please, correct your package.")

if not asterisks_failure_tests:
    log.notice("All needest lines contains asterisks")
