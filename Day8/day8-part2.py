#!/bin/python
import logging
import numpy as np

trees = []
bestview = 1
besttree = []

#set below to logging.DEBUG to see values line by line
logging.basicConfig(level=logging.DEBUG)
with open("input.txt", "r") as inFile:
    for i, line in enumerate(inFile):
        trees.append(i)
        trees[i] = list(map(int, f"{line.strip()}"))

n = np.array(trees)

for row in range(0, len(trees)):
    besttree.append(row)
    besttree[row] = []
    for column in range (0, len(trees[1])):
        besttree[row].append(column)
        comp = np.greater(trees[row][column], n)
        count = []
        val = 0
        if(column == 0): # Nothing is left of us
            count.append(1)
        else:
            for pos in range(column-1, -1, -1):
                val += 1
                if comp[row][pos] == False:
                    break
            count.append(val)
            
        val = 0
        if(column == len(trees[0])-1): # Nothing is right of us
            count.append(1)
        else:
            for pos in range(column+1, len(trees[0])):  
                val += 1
                if comp[row][pos] == False:
                    break
            count.append(val)

        val = 0
        if(row == 0): # Nothing is above us
            count.append(1)
        else:
            for pos in range(row-1, -1, -1):  
                val += 1
                if comp[pos][column] == False:
                    break
            count.append(val)

        val = 0
        if(row == len(trees) - 1): # Nothing is below us
            count.append(1)
        else:
            for pos in range(row+1, len(trees)):  
                val += 1
                if comp[pos][column] == False:
                    break
            count.append(val)

        view = count[0] * count[1] * count[2] * count[3]
        if bestview < view:
            bestview = view

        besttree[row][column] = view


logging.debug("Total Rows: %i", len(trees))
logging.debug("Column Width: %i", len(trees[0]))

logging.debug("Best: %i", bestview)
        
