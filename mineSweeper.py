from pprint import pprint
import random
from Queue import Queue

class Point:
    def __init__(self):
        self.val = 0
        self.isBomb = False
        self.visible = False

    def __repr__(self):
        if self.isBomb:
            return '*'
        else:
            return str(self.val)

class mineSweeper:
    def __init__(self, gridSize, numOfBombs):

        self.gridSize = gridSize
        self.grid = [[None for i in range(gridSize)] for j in range(gridSize)]

        # initialize the grid
        for r in range(gridSize):
            for c in range(gridSize):
                p = Point()
                self.grid[r][c] = p


        # initialize bombs randomly
        # also increment neighbour values
        for i in range(numOfBombs):
            r = random.randrange(gridSize)
            c = random.randrange(gridSize)


            self.grid[r][c].isBomb = True
            self.increment(r - 1, c - 1)
            self.increment(r - 1, c)
            self.increment(r - 1, c + 1)
            self.increment(r, c - 1)
            self.increment(r, c + 1)
            self.increment(r + 1, c - 1)
            self.increment(r + 1, c)
            self.increment(r + 1, c + 1)


        pprint(self.grid)

    def increment(self, r, c):
        if r < self.gridSize and c < self.gridSize and self.grid[r][c].isBomb == False:
            self.grid[r][c].val += 1

    def explore(self, r, c):
        ''' routine to run when user inputs a cordinate to play '''

        if self.grid[r][c].isBomb:
            # game over
            print 'Game Over!!'
            print
            self.Print(gameOver = True)
            return True
        elif self.grid[r][c].val > 0:
            self.grid[r][c].visible = True
            self.Print()
        elif self.grid[r][c].val == 0:
            # blank space, do BFS from here
            self.bfs(r,c)
            self.Print()

        return False

    def Print(self, gameOver = False):
        for r in range(self.gridSize):
            for c in range(self.gridSize):
                if gameOver or self.grid[r][c].visible:
                    print self.grid[r][c],
                else:
                    print 'H',
            print

    def bfs(self, r, c):
        ''' start bfs from r,c '''

        # mark all nodes as unvisited
        visited = [[False for i in range(self.gridSize)] for j in range(self.gridSize)]

        # push the start node to the queue
        traverseQueue = Queue()
        traverseQueue.put((r,c))

        # while queue is not empty
        while not traverseQueue.empty():
            # pop from the queue
            v = traverseQueue.get()

            pprint(v)

            r = v[0]
            c = v[1]

            # if r,c in grid
            if r < self.gridSize and c < self.gridSize:
                # if not visited
                if not visited[r][c]:
                    # mark it as visited
                    visited[r][c] = True

                    if self.grid[r][r].isBomb:
                        break

                    if self.grid[r][c].val > 0:
                        break


                    self.grid[r][c].visible = True

                    # enqueue the neighbours

                    traverseQueue.put((r - 1, c - 1))
                    traverseQueue.put((r - 1, c))
                    traverseQueue.put((r - 1, c + 1))

                    traverseQueue.put((r, c - 1))
                    traverseQueue.put((r, c + 1))

                    traverseQueue.put((r + 1, c - 1))
                    traverseQueue.put((r + 1, c))
                    traverseQueue.put((r + 1, c + 1))







