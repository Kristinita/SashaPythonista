# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2017-12-31 15:43:57
# @Last Modified time: 2017-12-31 22:34:46
# Check, if blabla in OS

import glob

import chardet

# Get all .txt file in a directory
# https://stackoverflow.com/a/3964689/5951529
globus = glob.glob('*.txt')

# Get list all filenames in a directory
# https://stackoverflow.com/a/1120736/5951529

for filename in globus:

    # Check if string in a file
    # https://stackoverflow.com/a/4944929/5951529
    #
    # exit code(1)
    # https://stackoverflow.com/a/9426054/5951529
    if '<body>' in open(filename).read():
        print(filename + " true")
    else:
        print("Filename " + filename + " not contain \\<body\\> . Please, add \
           \\<body\\> in " + filename)
        exit(1)

    # Not 100%, see https://stackoverflow.com/a/436299/5951529
    # Can doesn't work for Latin packages
    # Check decoding — https://chardet.readthedocs.io/en/latest/usage.html#example-using-the-detect-function
    # https://stackoverflow.com/a/37531241/5951529
    rawdata = open(filename, "rb").read()
    chardet_data = chardet.detect(rawdata)
    # Python dictionary
    fileencoding = (chardet_data['encoding'])
    print(fileencoding)

    if fileencoding == 'windows-1251':
        print(filename + " in windows-1251 encoding")
    else:
        print(filename + " not in windows-1251 encoding. Please, save a file \
           in windows-1251.")
        exit(1)

    # Lines to list
    # https://stackoverflow.com/a/3277515/5951529
    with open(filename) as f:
        lines = f.readlines()
        print(lines)
        # New list after <body>
        # https://stackoverflow.com/a/35880897/5951529
        get_index = lines.index('<body>\n')
        without_get = lines[get_index + 1:]
        # Remove list item, contains «<!--»
        # https://stackoverflow.com/a/3416473/5951529
        banger = [x for x in without_get if not '<!--' in x]
        print(banger)
        # Check all elements of list, that contains «*»
        # https://stackoverflow.com/a/44118151/5951529
        # print incorrect list items
        if all('*' in item for item in banger):
            print("All lines contains asterisks")
        else:
            not_asterisk_list_items = [item for item in banger if '*' not in
                                       item]
            print(not_asterisk_list_items)
            # Remove \n symbol in end of the lines
            # https://stackoverflow.com/a/30881893/5951529
            stripped_list = list(
                map(str.strip, not_asterisk_list_items))
            print(stripped_list)
            # Lists to strings with qoutes
            # https://stackoverflow.com/a/13207725/5951529
            list_to_strings = str(stripped_list)[1:-1]
            print("This lines not contains asterisks: " + list_to_strings)
            exit(1)
