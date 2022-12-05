"""
DAY 03: Find the total priorities of each for the packed rucksacks\

Challenge: https://adventofcode.com/2022/day/3
Input: https://adventofcode.com/2022/day/3/input

Notes:
    - busy day, part 1 only for now!
"""
import string

def handledata(inputdata):
    """
    Read the data from the text file and convert it into a list of lists
    New list of list converts letter inputs to "rock", "paper", "scissors"
    :param inputdata: input text file
    :return: sorted list of list
    """
    rucksackdata = []
    file = open(inputdata, "r").read().split('\n')
    for line in file:
        rucksackdata.append(line.split())
    return rucksackdata

def findsimilaritemvalue(rucksackinput, prioritiesdict):
    """
    Function to find the similar item between the two compartments of a bag
    We use // to round down the result from the division
    :param rucksackinput: string input, first half of string goes in compartment 1, second in compartment 2
    :return: the string of the similar item
    """
    comp1, comp2 = rucksackinput[:len(rucksackinput)//2], rucksackinput[len(rucksackinput)//2:]
    commonletter = ''.join(set(comp1).intersection(comp2))
    return prioritiesdict[commonletter]

def findsimilargroupvalue(groupinput, prioritiesdict):
    """
    Find the similar character from a list of three strings
    :param grouinput: list of three strings
    :param prioritiesdict: dictionary of priorities for each item
    :return: common item's value
    """
    commonletter = set.intersection(*map(set,groupinput))
    return prioritiesdict[commonletter]

if __name__ == "__main__":
    # PART 1
    priorities = dict()
    for i, letter in enumerate(string.ascii_letters):
        priorities[letter] = i + 1

    rucksackdata = handledata("Resources/03_a_input.txt")
    rucksackpriorities = []

    for i in range(len(rucksackdata)-1):
        rucksackpriorities.append(findsimilaritemvalue(rucksackdata[i][0],priorities))

    print('Total priority value is:', sum(rucksackpriorities))
