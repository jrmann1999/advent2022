#!/bin/python

count = 0
secondcount = 0
thirdcount = 0

with open("input.txt", "r") as inFile:
    inCount = 0
    for line in inFile:
        if line is '\n':
            if inCount > count:
                thirdcount = secondcount
                secondcount = count
                count = inCount
                inCount = 0
            elif inCount > secondcount:
                thirdcount = secondcount
                secondcount = inCount
                inCount = 0
            elif inCount > thirdcount:
                thirdcount = inCount
                inCount = 0
            elif count == 0:
                count = inCount
                inCount = 0
            else:
                inCount = 0
        else:
            inCount += int(line.strip(), base=10)


print(count, secondcount, thirdcount)
print(count + secondcount + thirdcount)
    