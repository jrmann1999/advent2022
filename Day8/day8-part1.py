#!/bin/python
import logging
import numpy as np

trees = []

#set below to logging.DEBUG to see values line by line
logging.basicConfig(level=logging.DEBUG)
with open("input.txt", "r") as inFile:
    for i, line in enumerate(inFile):
        trees.append(i)
        trees[i] = list(map(int, f"{line.strip()}"))

n = np.array(trees)

total = 0

for row in range(0, len(trees)):
    for column in range (0, len(trees[1])):
        if row == 0 or column == 0:
            total += 1
            logging.debug("ROW/COLUMN Border: %i, %i, %i, %i", row, column, trees[row][column], total)
            continue
        elif row == len(trees) - 1 or column == len(trees[0]) - 1:
            total += 1
            logging.debug("ROW/COLUMN Border: %i, %i, %i, %i", row, column, trees[row][column], total)
            continue
        comp = np.greater(trees[row][column], n)
        if False in comp[row,:column]:
            next
        else:
            total += 1
            logging.debug("%i, %i, %i, %i, LEFT", row, column, trees[row][column], total)
            continue
        if False in comp[row,column+1:]:
            next
        else:
            total += 1
            logging.debug("%i, %i, %i, %i, RIGHT", row, column, trees[row][column], total)
            continue
        if False in comp[row+1:,column]:
            next
        else: 
            total += 1
            logging.debug("%i, %i, %i, %i, DOWN", row, column, trees[row][column], total)
            continue
        if False in comp[:row,column]:
            next
        else:
            total += 1
            logging.debug("%i, %i, %i, %i, UP", row, column, trees[row][column], total)
            continue

logging.debug("Total Rows: %i", len(trees))
logging.debug("Column Width: %i", len(trees[0]))

logging.debug("Total: %i", total)
        
