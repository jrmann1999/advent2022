#!/bin/python

import logging

total = 0

linecount = 0
lineary = []
#set below to logging.DEBUG to see values line by line
logging.basicConfig(level=logging.DEBUG)
with open("input.txt", "r") as inFile:
    for line in inFile:
        linecount += 1
        lineary.append(line.strip())
        if(linecount > 2):
            logging.debug(lineary)
            common = set(lineary[0]).intersection(lineary[1]).intersection(lineary[2])
            logging.debug(common)

            commonstring = str(common.pop())
            logging.debug(commonstring)
            if(commonstring.islower()):
                value = ord(commonstring) - 96
            else:
                value = ord(commonstring) - 38
            logging.debug(value)

            if(value < 0):
                logging.info(commonstring)
            total += value

            lineary = []
            linecount = 0

print(total)

