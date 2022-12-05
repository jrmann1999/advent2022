#!/bin/python
import logging
import queue
import re

#set below to logging.DEBUG to see values line by line
logging.basicConfig(level=logging.INFO)
with open("inputorig.txt", "r") as inFile:
    stacks, commands= inFile.read().strip().split('\n\n')
    
#split stacks string into rows, grab last row to know how many columns
columns = stacks.split('\n')[-1:]
logging.debug("Columns: %s", columns[0])

# convert columns into a set, to determine how many columns there are.  There can be
# a hanging space, so I pull that out of the resultant set
colset = set(columns[0]).difference(' ')
logging.debug("Unique columns (set): %s", colset)
logging.debug("Number of columns: %i", len(colset)) # Length of the set


# build an array, that will hold my queues in order (1-#)
ship = []
for i in range(0, len(colset)):
    q = queue.LifoQueue()
    ship.append(q)

logging.debug("Array of queues: %s",ship)

#split the bit stacks string by newline, this will give me rows.  Ignore last row
newstacks = stacks.split('\n')[:-1]

# I want these in reverse order, so my LIFO queue will have the proper order
for row in newstacks[::-1]:
    # normalize graph, substituting [ ] for empty strings
    sub = ''
    # Read 4 characters at a time, this is the format [X]_ where _ is space
    for i in range(0, len(row) - 1, 4): 
        if(row[i:i+4].strip() == ''):
            sub += '[ ],'
        else:
            sub += row[i:i+4].strip() + ','
    
    for i, entry in enumerate(sub[:-1].split(',')):
        #skip blanks when building queue
        if('[ ]' in entry):
            continue
        
        ship[i].put(entry)

# Now that we have the graph in a queue, we can start moves (using commands from above)
for line in commands.split('\n'):
    logging.debug(line.strip())
    d = re.search('^\w+ (\d+) \w+ (\d+) \w+ (\d+)', line.strip())
    if(d):
        nummoves = int(d[1])
        start = int(d[2]) - 1
        end = int(d[3]) - 1
        logging.debug("BEGIN: SHIP_START[%d]: %s", start, ship[start].queue)
        logging.debug("BEGIN: SHIP_END[%d]: %s", end, ship[end].queue)
        for i in range(1, nummoves + 1):
            ship[end].put(ship[start].get())
        logging.debug("END: SHIP_START[%d]: %s", start, ship[start].queue)
        logging.debug("END: SHIP_END[%d]: %s", end, ship[end].queue)

endstr = ''
for entry in ship:
    endstr += entry.get()

print(endstr.replace('[', '').replace(']', ''))
          
