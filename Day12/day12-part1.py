import logging


# Most of this was solved in https://www.reddit.com/r/adventofcode/comments/zjte21/2022_day_12_part_1python_good_answer_for_test/ and I used that code

#set below to logging.DEBUG to see values line by line
logging.basicConfig(level=logging.DEBUG)

from collections import deque

def neighbours(grid, x, y):
    for (dx, dy) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if all((x+dx >= 0, x+dx < len(grid), y+dy >= 0, y+dy < len(grid[0]))):
	        yield(x+dx, y+dy)

def find_path(grid, start, goal):
    visited = set()
    queue = deque([(start, 0)])
    
    while len(queue):
        pt, dist = queue.popleft()

        if pt not in visited:
            visited.add(pt)
            
            if pt == goal:
                return dist

            else:
                for n in neighbours(grid, *pt):
                    if grid[n[0]][n[1]] - grid[pt[0]][pt[1]] <= 1:
                        queue.append((n, dist+1))
    return -1


with open("input.txt", "r") as inFile:
    grid = [[-1 if c == 'S' else 26 if c == 'E' else ord(c) - ord('a') 
            for c in l.strip()] for l in inFile.readlines()]

    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == -1:
                start = (i, j)
            elif val == 26:
                goal = (i, j)
    
    print('Part 1:', find_path(grid, start, goal))
