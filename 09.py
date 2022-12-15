"""
DAY 09: Find the movements of the rope bridge

Challenge: https://adventofcode.com/2022/day/9
Input: https://adventofcode.com/2022/day/9/input

Notes:
    - so...this code is not pretty
    - approach was to build a large grid (2D array) - ended up overriding this with a 1000 x 1000 because the targeted on was too small
    - grid contains zeros only
    - head and tail move around the grid, everytime the tail moves, it sets it's new square to 1
    - total of all values in grid equals number of cells that the tail moved into

    - would like to re-do this one in a more efficient way!

    - second half not yet attempted
"""
import numpy as np

def handledata(inputdata):
    """
    Read the data from the text file - list of lists, each list is a line of forest treet
    :return: string from input
    """
    file = open(inputdata, "r").read().splitlines()
    data = [line.split(' ') for line in file]
    return data

class TheRopeGrid():
    def __init__(self, moves):
        self.moves = moves
        self.grid = np.zeros((1000, 1000), dtype=int) # grid that we move around, assume we wont move outside of a 1000x1000 grid - lazy i know
        self.x = [500, 500] # head position, tail position
        self.y = [500, 500] # head position, tail position
        self.xmax = 0
        self.ymax = 0
        self.size = [0, 0, 0, 0]  # xmin, xmax, ymin, ymax
        self.diffx = 0
        self.diffy = 0

    def checklocal(self):
        self.diffx = self.x[0] - self.x[1]
        self.diffy = self.y[0] - self.y[1]
        if abs(self.diffx) < 2 and abs(self.diffy) < 2:
            return True
        else:
            return False

    def updategrid(self):
        if not self.checklocal():
            if self.x[0] == self.x[1]: # move in y only
                print('y move')
                self.y[1] += int((self.y[0] - self.y[1]) / 2)
                self.grid[self.y[1]][self.x[1]] = 1
            elif self.y[0] == self.y[1]: # move in x only
                print('x move')
                self.x[1] += int((self.x[0] - self.x[1]) / 2)
                self.grid[self.y[1]][self.x[1]] = 1
            else: # a super inefficient way of dealing diagonal moves
                print('diagonal move')
                if (self.diffx == -1 and self.diffy == 2) or (self.diffx == -2 and self.diffy == 1):
                    self.x[1] -= 1
                    self.y[1] += 1
                elif (self.diffx == 1 and self.diffy == -2) or (self.diffx == 2 and self.diffy == -1):
                    self.x[1] += 1
                    self.y[1] -= 1
                elif (self.diffx == 1 and self.diffy == 2) or (self.diffx == 2 and self.diffy == 1):
                    self.x[1] += 1
                    self.y[1] += 1
                elif (self.diffx == -1 and self.diffy == -2) or (self.diffx == -2 and self.diffy == -1):
                    self.x[1] -= 1
                    self.y[1] -= 1
                self.grid[self.y[1]][self.x[1]] = 1

    def run(self):
        for move in self.moves:
            if move[0] == 'L':
                for i in range(int(move[1])):
                    self.x[0] -= 1
                    self.updategrid()
            elif move[0] == 'R':
                for i in range(int(move[1])):
                    self.x[0] += 1
                    self.updategrid()
            elif move[0] == 'D':
                for i in range(int(move[1])):
                    self.y[0] += 1
                    self.updategrid()
            elif move[0] == 'U':
                for i in range(int(move[1])):
                    self.y[0] -= 1
                    self.updategrid()

        return 1 + sum(map(sum, self.grid)) # Add 1 for initial start position


if __name__ == "__main__":
    # PART 1
    moves = handledata("Resources/09_a_input.txt")
    print(moves)

    RopeyBridge = TheRopeGrid(moves)
    totalcells = RopeyBridge.run()
    print("Total cells tail moves through is: ", totalcells)