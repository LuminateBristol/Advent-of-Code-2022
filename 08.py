"""
DAY 08: Find the number of visible trees in the forest

Challenge: https://adventofcode.com/2022/day/8
Input: https://adventofcode.com/2022/day/8/input

Notes:
    -
"""
import numpy as np
import math


def handledata(inputdata):
    """
    Read the data from the text file - list of lists, each list is a line of forest treet
    :return: string from input
    """
    file = open(inputdata, "r").read().splitlines()
    data = [list(map(int, line)) for line in file]
    data = np.array(data)
    return data

def visibletrees(forest):
    """
    Return the total number of visible trees from all sides
    :param forest: list of list with tree data in it
    :return: total number of visible trees
    """
    y = len(forest)
    x = len(forest[0])
    visible = np.zeros((x, y), dtype=int)
    # Check elements one by one
    for i in range(y):
        for j in range(x):
            if 0 < i < y-1 and 0 < j < x-1:
                if forest[i][j] > max(forest[i, 0:j]) or forest[i][j] > max(forest[i, j+1:x]) or forest[i][j] > max(forest[0:i, j]) or forest[i][j] > max(forest[i+1:y, j]):
                    visible[i][j] = 1

    # Add up outer trees which are always visible plus the inner visble trees calculated above
    visibletotal = 2*x + 2*y - 4 + sum(map(sum, visible))
    return visibletotal

def treehouse(forest):
    """
    Return the tree best tree house location based on how far each tree can see north, east, south and west
    :param forest: list of lists of tree data
    :return: top score tree
    """
    y = len(forest)
    x = len(forest[0])
    totalscores = np.zeros((x, y), dtype=int) # For each tree this will be populated with its score
    for i in range(y):
        for j in range(x):
            iorig = i
            jorig = j

            totalscores[iorig][jorig] =

    print(totalscores.argmax())
    return totalscores.argmax()






if __name__ == "__main__":
    # PART 1
    trees = handledata("Resources/08_a_input.txt")
    print("The total number of visible trees is: ", visibletrees(trees))

    # PART 2
    treehouse(trees)

