import logging
import numpy as np

global bridge
bridge = [] # We will dynamically create the bridge as movements progress.
bridge.append(0)
bridge[0] = []
bridge[0].append('')
bridge[0][0] = 'H'

global posary
posary = {}
for entry in range(1,10):
    posary[entry] = [0,0]
    
#set below to logging.DEBUG to see values line by line
logging.basicConfig(level=logging.DEBUG)
inFile = open("inputsmall.txt", "r")
moves = inFile.readlines()

curHeadcolumn = 0 # We need to track our H position
curHeadrow = 0 # We need to track our H position
curTailcolumn = 0 # We need to track our T position
curTailrow = 0 # We need to track our T position


def mark(row, col, m):
    if bridge[row][col] != "#":
        bridge[row][col] = m

def movemap(row, col, marker):
    if marker == 9:
        mark(posary[mark][0],posary[mark][1],'#')
        posary[mark][0] = posary[mark-1][0]
        posary[mark][1] = posary[mark-1][1]
    else:
        
        mark(row,col,'H') # Mark the head
        for i in range (1, 10):
            movemap(posary[], col, parentrow, parentcol, i)
    elif mark in '12345678':
        if abs(parentrow - row) > 1 or abs(parentcol - col) > 1:
            if curTailrow != curHeadrow: 
                bridge[curTailrow][curTailcolumn] = '#' # Mark the tail 
                curTailrow = curHeadrow # Diagonal move just happened, move the tail up or down
                curTailcolumn += 1
            else: # Head move to the right away from tail
                mark(curTailrow,curTailcolumn,'#') # Mark where the tail was
                curTailcolumn += 1

        dosomething()
    elif mark == '9':
        # Mark the #


for movenum, entry in enumerate(moves):
    dir,amount = entry.strip().split()
    amount = int(amount)
    logging.debug("%s %i", dir, amount)

    if dir == 'R':
        if curHeadcolumn + amount > len(bridge[curHeadrow]) - 1: # We need to expand the bridge to the right
            logging.debug("EXPAND RIGHT:%s %i", dir, amount)
            for i in range(amount):
                for row in range(len(bridge)): # We're expanding ALL rows, not just current
                    bridge[row].append(".")  

        for move in range(amount):
            movemap(curHeadrow, curHeadcolumn, curHeadrow, curHeadcolumn + 1, 0)
            
            if abs(curHeadcolumn - curTailcolumn) > 1:
                if curTailrow != curHeadrow: 
                    bridge[curTailrow][curTailcolumn] = '#' # Mark the tail 
                    curTailrow = curHeadrow # Diagonal move just happened, move the tail up or down
                    curTailcolumn += 1
                else: # Head move to the right away from tail
                    mark(curTailrow,curTailcolumn,'#') # Mark where the tail was
                    curTailcolumn += 1
        mark(curTailrow,curTailcolumn,'#') # Mark the tail 

    elif dir == 'L':
        if curHeadcolumn - amount < 0: # Expand left
            logging.debug("EXPAND LEFT:%s %i", dir, amount)
            for i in range (amount):
                for row in bridge:
                    row.insert(0, '.')
                curHeadcolumn += 1
                curTailcolumn += 1
            
        for move in range(amount):
            mark(curHeadrow,curHeadcolumn,'.') # Unmark the head
            curHeadcolumn -= 1
            mark(curHeadrow,curHeadcolumn,'H') # Mark the head
            if abs(curHeadcolumn - curTailcolumn) > 1:
                if curTailrow != curHeadrow: 
                    bridge[curTailrow][curTailcolumn] = '#' # Mark the tail 
                    curTailrow = curHeadrow # Diagonal move just happened, move the tail up or down
                    curTailcolumn -= 1
                else: # Head move to the right away from tail
                    mark(curTailrow,curTailcolumn,'#') # Mark where the tail was
                    curTailcolumn -= 1
        mark(curTailrow,curTailcolumn,'#') # Mark the tail 
    
    elif dir == 'U':
        if curHeadrow + amount > len(bridge) - 1: #We will cross the top, time to make the bridge longer
            logging.debug("EXPAND UP:%s %i", dir, amount)
            for j in range(amount):
                newrow = []
                for i in range(len(bridge[0])):
                    newrow.append(".")
                bridge.insert(len(bridge), newrow)
        
        for move in range(amount):
            mark(curHeadrow,curHeadcolumn,'.') # Unmark the head
            curHeadrow += 1
            mark(curHeadrow,curHeadcolumn,'H') # Mark the head
            if abs(curHeadrow - curTailrow) > 1:
                if curTailcolumn != curHeadcolumn: 
                    mark(curTailrow,curTailcolumn,'#') # Mark where the tail was
                    curTailcolumn = curHeadcolumn # Diagonal move just happened, move the tail left or right
                    curTailrow += 1
                else: # Head move up away from tail
                    mark(curTailrow,curTailcolumn,'#') # Mark where the tail was
                    curTailrow += 1
        mark(curTailrow,curTailcolumn,'#') # Mark the tail 

    elif dir == 'D':
        if curHeadrow - amount < 0: # Expand Down (backwards??)
            logging.debug("EXPAND DOWN:%s %i", dir, amount)
            for i in range(amount):
                newrow = []
                for entry in bridge[0]:
                    newrow.append(".")
                bridge.insert(0, newrow)
                curHeadrow += 1
                curTailrow += 1
        
        for move in range(amount):
            mark(curHeadrow,curHeadcolumn,'.') # Unmark the head
            curHeadrow -= 1
            mark(curHeadrow,curHeadcolumn,'H') # Mark the head
            if abs(curHeadrow - curTailrow) > 1:
                if curTailcolumn != curHeadcolumn: 
                    mark(curTailrow,curTailcolumn,'#') # Mark where the tail was
                    curTailcolumn = curHeadcolumn # Diagonal move just happened, move the tail left or right
                    curTailrow -= 1
                else: # Head move up away from tail
                    mark(curTailrow,curTailcolumn,'#') # Mark where the tail was
                    curTailrow -= 1
        mark(curTailrow,curTailcolumn,'#') # Mark the tail 


n = np.array(bridge)
occur = np.count_nonzero(n == '#')
print(occur) 



