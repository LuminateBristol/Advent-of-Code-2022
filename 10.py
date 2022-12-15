"""
DAY 10:

Challenge: https://adventofcode.com/2022/day/10
Input: https://adventofcode.com/2022/day/10/input

Notes:
    - first half done
    - second half not yet attempted
"""

def handledata(inputdata):
    """
    Read the data from the text file - list of lists, each list is a line of forest treet
    :return: string from input
    """
    file = open(inputdata, "r").read().splitlines()
    data = [line.split(' ') for line in file]
    return data

def signalstrength(inputcycles):
    records = [20, 60, 100, 140, 180, 220]
    total = []
    cycle = 0
    x = 1
    for line in inputcycles:
        if line[0] == 'noop':
            cycle += 1
            if cycle in records:
                total.append(x)
        elif line[0] == 'addx':
            cycle += 1
            if cycle in records:
                total.append(x)
            cycle += 1
            if cycle in records:
                total.append(x)
            x += int(line[1])

    finaltotal = sum(x * y for x, y in zip(records, total))
    return finaltotal

if __name__ == "__main__":
    # PART 1
    cycles = handledata("Resources/10_a_input.txt")
    print(cycles)

    total = signalstrength(cycles)
    print(total)