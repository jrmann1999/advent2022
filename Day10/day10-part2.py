import logging

#set below to logging.DEBUG to see values line by line
logging.basicConfig(level=logging.DEBUG)

global XReg
global Cycle
global Sprite
XReg = 1
Cycle = 1
Sprite = '.' * 40
CRT = [Sprite]


def drawSprite():
    if XReg <=1:
        return ('###' + '.'*37)
    elif XReg >=39:
        return ('.'*37 + '###')
    else:
        return ('.'*(XReg-1) + '###' + '.'*(40-(3+(XReg-1))))


inFile = open("input.txt", "r")
codes = inFile.readlines()
CycleDiv = 0
CRTROW = 0
for i, line in enumerate(codes):
    Sprite = drawSprite()
    logging.debug(Sprite)
        
    if line.strip() == 'noop':
        if (Cycle-1)%40 == 0 and Cycle > 1:
            CRTROW += 1
            CRT.append('.'*40)
            CycleDiv += 1
        if((Cycle-1)-(CycleDiv*40)) in (0, 40):
            newCRT = Sprite[0]
        else:
            key = int((Cycle-(CycleDiv*40)-1))
            newCRT = CRT[CRTROW][:key] + Sprite[key]
        CRT[CRTROW] = newCRT
        Cycle += 1
        continue

    addline = line.strip().split()

    if addline[0] == 'addx':
        for counter in (0, 1):
            #Sprite = drawSprite()
            if (Cycle-1)%40 == 0 and Cycle > 1:
                CRTROW += 1
                CRT.append('.'*40)
                CycleDiv += 1

            if((Cycle-1)-(CycleDiv*40)) == 40:
                newCRT = Sprite[0]
            else:
                key = int((Cycle-(CycleDiv*40))-1)
                newCRT = CRT[CRTROW][:key] + Sprite[key]

            CRT[CRTROW] = newCRT
            Cycle += 1
        XReg += int(addline[1])

for entry in (CRT):
    print(entry)