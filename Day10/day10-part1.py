import logging

#set below to logging.DEBUG to see values line by line
logging.basicConfig(level=logging.DEBUG)
inFile = open("input.txt", "r")
codes = inFile.readlines()

XReg = 1
Cycle = 1

def printCycle(c, x):
    cycles = (20, 60, 100,140, 180, 220)
    print(f"XReg: {x}")
    if c in cycles:
        print(f"Cycle {c}: {c*x}")


    

for i, line in enumerate(codes):
    printCycle(Cycle, XReg)
        
    if line.strip() == 'noop':
        Cycle += 1
        continue

    addline = line.strip().split()

    if addline[0] == 'addx':
        printCycle(Cycle+1, XReg)
        Cycle += 2
        XReg += int(addline[1])
