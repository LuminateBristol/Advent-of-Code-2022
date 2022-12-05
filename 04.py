"""
DAY 04: Find the overlapping camp cleanups for pairs of elves
Challenge: https://adventofcode.com/2022/day/4
Input: https://adventofcode.com/2022/day/4/input

Notes:
    - cheated a bit and used re
    - there is definitely a neater way to do this...
"""

import re

def handledata(inputdata):
    """
    Read the data from the text file and convert it into a list of lists
    New list of list converts letter inputs to "rock", "paper", "scissors"
    :param inputdata: input text file
    :return: sorted list of list
    """
    data = []
    file = open(inputdata, "r").read().split('\n')
    file.pop() # Remove last empty line
    for line in file:
        data.append(line.split())
    return data

def calculatefulloverlaps(cleaningdata):
    """"""
    fulloverlaps = 0
    for i in cleaningdata:
        elfsects = [int(j) for j in re.findall(r'\d+', i[0])]   # Use re.findall to extract integers from string and put them into a list
        if (elfsects[0] >= elfsects[2] and elfsects[1] <= elfsects[3]) or (elfsects[0] <= elfsects[2] and elfsects[1] >= elfsects[3]):
            fulloverlaps += 1
    return fulloverlaps

def calculatepartoverlaps(cleaningdata):
    """"""
    partoverlaps = 0
    for i in cleaningdata:
        elfsects = [int(j) for j in
                    re.findall(r'\d+', i[0])]  # Use re.findall to extract integers from string and put them into a list
        if elfsects[2]<=elfsects[0]<=elfsects[3] or elfsects[2]<=elfsects[1]<=elfsects[3] or elfsects[0]<=elfsects[2]<=elfsects[1] or elfsects[0]<=elfsects[3]<=elfsects[1]:
            partoverlaps += 1
    return partoverlaps

if __name__ == "__main__":
    # PART 1
    cleaningdata = handledata("Resources/04_a_input.txt")
    totaloverlaps = calculatefulloverlaps(cleaningdata)
    print("The total number of full overlaps within the pairs is:", totaloverlaps)

    # PART 2
    partoverlaps = calculatepartoverlaps(cleaningdata)
    print("The total number of partial overlaps within the pairs is:", partoverlaps)