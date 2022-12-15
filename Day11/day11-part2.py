#!/bin/python

import logging

def numeric(Item, equation):
    if 'old' in equation:
        equation = equation.replace('old', str(Item))

    if '+' in equation:
        y = equation.split('+')
        x = int(y[0])+int(y[1])
    elif '-' in equation:
        y = equation.split('-')
        x = int(y[0])-int(y[1])
    elif '*' in equation:
        y = equation.split('*')
        x = int(y[0])*int(y[1])
    elif '/' in equation:
        y = equation.split('/')
        x = int(y[0])/int(y[1])
    return x

#set below to logging.DEBUG to see values line by line
logging.basicConfig(level=logging.DEBUG)
inFile = open("input.txt", "r")
codes = inFile.readlines()
Monkies = []
for i in range(0, len(codes), 7):
    Monkey = codes[i:i+7]

    MonkeyNum = int(Monkey[0].rstrip().split()[1][0])
    Monkies.append(MonkeyNum)
    Monkies[MonkeyNum] = {}
    Monkies[MonkeyNum]['Items'] = [int(ele) for ele in Monkey[1].lstrip().split(":")[1].strip().replace(" ", "").split(",")]
    Monkies[MonkeyNum]['Ops'] = Monkey[2].lstrip().split(":")[1].strip().lstrip().split("=")[1].strip().split()[1:]
    Monkies[MonkeyNum]['Test'] = int(Monkey[3].lstrip().split(":")[1].strip().split()[2])
    Monkies[MonkeyNum][True] = int(Monkey[4].lstrip().split(":")[1].strip().split()[3])
    Monkies[MonkeyNum][False]  = int(Monkey[5].lstrip().split(":")[1].strip().split()[3])
    Monkies[MonkeyNum]['Inspect'] = 0

supermod = 0
for Monkey in Monkies:
    supermod += Monkey['Test']

logging.debug("Supermod: %i", supermod)

for i in range(0, 10000):
    #logging.debug(Monkies)
    for Monkey in Monkies:
        #logging.debug("PRE:%s", Monkey)

        for Item in Monkey['Items']:
            Monkey['Inspect'] += 1
            Worry = numeric(str(Item), str(Item) + Monkey['Ops'][0] + Monkey['Ops'][1])
            Worry = Worry % supermod
            if Worry % Monkey['Test'] == 0:
                Monkies[Monkey[True]]['Items'].append(Worry)
            else:
                Monkies[Monkey[False]]['Items'].append(Worry)
    
        Monkey['Items'] = []
        #logging.debug("POST:%s", Monkey)

for Monkey in Monkies:
    print(Monkey['Inspect'])