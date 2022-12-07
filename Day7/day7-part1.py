#!/bin/python
import logging
import queue

total = 0
dirtree = {}
parent = ''
dirqueue = queue.LifoQueue()
dirtree['/'] = {}
dirtree['/']['dir'] = []
dirtree['/']['file'] = []
dirtree['/']['size'] = 0


def findbigdirs(tree, key):
    global total
    dirqueue.put(key)
    path = ":".join(dirqueue.queue)
    size = tree[path]['size']
    for entry in tree[path]['dir']:
        #logging.debug(entry)
        size += findbigdirs(tree, entry)

    if size < 100000:
        logging.debug('DIR, Size: %s %i', path, size)
        total += size

    dirqueue.get()
    return size

                

#set below to logging.DEBUG to see values line by line
logging.basicConfig(level=logging.DEBUG)
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

#logging.debug(dirtree)

dirqueue = queue.LifoQueue()
size = findbigdirs(dirtree, '/')
logging.debug(size)
logging.debug(total)




