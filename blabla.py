# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2017-12-31 15:43:57
# @Last Modified time: 2017-12-31 17:15:13
# Check, if blabla in OS

import glob

# Get all .txt file in a directory
# https://stackoverflow.com/a/3964689/5951529
globus = glob.glob('*.txt')

# Get list all filenames in a directory
# https://stackoverflow.com/a/1120736/5951529

for filename in globus:

    # Check if string in a file
    # https://stackoverflow.com/a/4944929/5951529
    if 'blabla' in open(filename).read():
        print(filename + " true")
    else:
        print(filename + " false")
        exit(0)
