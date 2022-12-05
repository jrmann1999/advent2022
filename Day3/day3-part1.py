#!/bin/python

import logging

total = 0

#set below to logging.DEBUG to see values line by line
logging.basicConfig(level=logging.INFO)
with open("input.txt", "r") as inFile:
    for line in inFile:
        data = line.strip()
        logging.debug(data)
        half = int(len(data)/2)
        logging.debug(half)
        firsthalf = data[:half]
        logging.debug(firsthalf)
        secondhalf = data[half:]
        logging.debug(secondhalf)
        common = set(firsthalf).intersection(secondhalf)
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

print(total)

