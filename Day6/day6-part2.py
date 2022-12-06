#!/bin/python
import logging


#set below to logging.DEBUG to see values line by line
logging.basicConfig(level=logging.DEBUG)
with open("input.txt", "r") as inFile:
    data = inFile.readlines()

    logging.debug(data[0])

    logging.debug(type(data[0]))
    logging.debug(len(data[0]))
    for i in range(13, len(data[0])):
        logging.debug(data[0][i:i+14])
        if len(set(data[0][i:i+14])) == 14:
            print(i+14)
            break