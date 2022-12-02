"""
DAY 02: Find the total score of the rock paper scissors game when"
        A=1, B=2, C=3
        L=0, D=3, W=6
Challenge: https://adventofcode.com/2022/day/2
Input: https://adventofcode.com/2022/day/1/input

Notes:
    - went for the easy option and used if statements
    - this is horribly unreadable but it does work
    - better solution would be with dicts
"""

# FUNCTIONS
def handledata(inputdata):
    """
    Read the data from the text file and convert it into a list of lists
    New list of list converts letter inputs to "rock", "paper", "scissors"
    :param inputdata: input text file
    :return: sorted list of list
    """
    listolists = []
    file = open(inputdata, "r").read().split('\n')
    for line in file:
        listolists.append(line.split())
    return listolists

def findwinner(enemyelf, me):
    """
    Find the winner of the rock paper scissors between my oponent and me
    :param enemyelf: oponent input A, B or C
    :param me:  my input X, Y or Z
    :return: score for this round
    """
    if enemyelf == "A":
        if me == "X":
            return 3+1
        elif me == "Y":
            return 6+2
        elif me == "Z":
            return 0+3
    elif enemyelf == "B":
        if me == "X":
            return 0 + 1
        elif me == "Y":
            return 3 + 2
        elif me == "Z":
            return 6 + 3
    elif enemyelf == "C":
        if me == "X":
            return 6 + 1
        elif me == "Y":
            return 0 + 2
        elif me == "Z":
            return 3 + 3

def findoptimumchoice(enemyelf, cheatcode):
    """
    The sneaky elf has changed the rules.
    The second letter now means whether one should lose, draw or win
    :param enemyelf: enemy elf value, A, B or C
    :param cheatcode: optium choice of either X, Y or Z
    :return: choice for this round
    """
    if cheatcode == 'X':
        if enemyelf == 'A':
            return 'Z'
        elif enemyelf == 'B':
            return 'X'
        elif enemyelf == 'C':
            return'Y'
    if cheatcode == 'Y':
        if enemyelf == 'A':
            return 'X'
        elif enemyelf == 'B':
            return 'Y'
        elif enemyelf == 'C':
            return 'Z'
    if cheatcode == 'Z':
        if enemyelf == 'A':
            return 'Y'
        elif enemyelf == 'B':
            return 'Z'
        elif enemyelf == 'C':
            return 'X'

def calculatetotal(list):
    """
    Calculate the total score from the listolists
    :param list: the list of lists with the game outcomes. First column is elf, second is me.
    :return: total score
    """
    winlose = []
    for i in range(len(list) - 1):
        winlose.append(findwinner(list[i][0], list[i][1]))
    return sum(winlose)

if __name__ == "__main__":
    listolists = handledata("Resources/02_a_input.txt")

    # PART 1
    totalscore = calculatetotal(listolists)
    print("Total score for this game is:", totalscore)

    # PART 2
    for i in range(len(listolists) - 1):
        listolists[i][1] = findoptimumchoice(listolists[i][0], listolists[i][1])

    totalscore = calculatetotal(listolists)
    print("Total score for this new game is:", totalscore)