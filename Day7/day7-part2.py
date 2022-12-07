#!/bin/python
import logging
import queue

total = 0
smallest = 0
dirtree = {}
parent = ''
dirqueue = queue.LifoQueue()
dirtree['/'] = {}
dirtree['/']['dir'] = []
dirtree['/']['file'] = []
dirtree['/']['size'] = 0


def findsmalldirs(tree, key, sizeneeded):
    global total, smallest
    dirqueue.put(key)
    path = ":".join(dirqueue.queue)
    size = tree[path]['size']
    for entry in tree[path]['dir']:
        size += findsmalldirs(tree, entry, sizeneeded)

    if size > sizeneeded:
        logging.debug('DIR, Size: %s %i', path, size)
        if smallest == 0:
            smallest = size
        elif size < smallest:
            smallest = size

    dirqueue.get()
    return size

def findbigdirs(tree, key, sizeneeded):
    global total
    dirqueue.put(key)
    path = ":".join(dirqueue.queue)
    size = tree[path]['size']
    for entry in tree[path]['dir']:
        size += findbigdirs(tree, entry, sizeneeded)

    if size < sizeneeded:
        #logging.debug('DIR, Size: %s %i', path, size)
        total += size

    dirqueue.get()
    return size

                

#set below to logging.DEBUG to see values line by line
logging.basicConfig(level=logging.INFO)
file = 'input.txt'
with open(file, "r") as inFile:
    for line in inFile:
        lineary = line.strip().split(' ')
        if line[0] == '$':
            if lineary[1] == 'cd':
                if (lineary[2] == '..'):
                    dirqueue.get()
                else:
                    parent = ":".join(dirqueue.queue)
                    dirqueue.put(lineary[2])
                    path = ":".join(dirqueue.queue)
                        
                    if path not in dirtree:
                        dirtree[path] = {}
                        dirtree[path]['dir'] = []
                        dirtree[path]['file'] = []
                        dirtree[path]['size'] = 0
        elif line[0:3] == 'dir':
            path = ":".join(dirqueue.queue)
            dirtree[path]['dir'].append(lineary[1])
        else:
            path = ":".join(dirqueue.queue)
            
            dirtree[path]['file'].append(lineary[1])
            dirtree[path]['size']+= int(lineary[0])


dirqueue = queue.LifoQueue()
size = findbigdirs(dirtree, '/', 100000)
print("Total Size: ",size)
print("Total of Directories under 100000: ", total)



print("Total Drive: 70000000")
freespace = abs(70000000 - size)
print("Free Space: ", freespace)
sizeneeded = 30000000 - freespace
print("Size Required: ", sizeneeded)

size = findsmalldirs(dirtree, '/', sizeneeded)
print("Smallest Folder is: ", smallest)