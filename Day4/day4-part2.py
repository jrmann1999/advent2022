#!/bin/python

import logging

total = 0

#set below to logging.DEBUG to see values line by line
logging.basicConfig(level=logging.DEBUG)
with open("input.txt", "r") as inFile:
    for line in inFile:
        (a, b) = line.strip().split(',')
        arange = range(int(a.split('-')[0]), int(a.split('-')[1]) + 1)
        brange = range(int(b.split('-')[0]), int(b.split('-')[1]) + 1)
        logging.debug('%s, %s', arange, brange)

        if len(set(arange).intersection(brange)) > 0:
            total += 1

print(total)
      