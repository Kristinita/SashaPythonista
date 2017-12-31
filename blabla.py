# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2017-12-31 15:43:57
# @Last Modified time: 2017-12-31 19:04:11
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
    if 'blabla' in open(filename).read():
        print(filename + " true")
    else:
        print("Filename " + filename + " not contain \\<body\\> . Please, add \
           \\<body\\> in " + filename)
        exit(1)

    # Not 100%, see https://stackoverflow.com/a/436299/5951529
    # Check decoding — https://chardet.readthedocs.io/en/latest/usage.html#example-using-the-detect-function
    # https://stackoverflow.com/a/37531241/5951529
    rawdata = open(filename, "rb").read()
    chardet_data = chardet.detect(rawdata)
    # Python словарь
    fileencoding = (chardet_data['encoding'])

    if fileencoding == 'windows-1251':
        print(filename + " in windows-1251 encoding")
    else:
        print(filename + " not in windows-1251 encoding. Please, save a file \
           in windows-1251.")
        exit(1)
