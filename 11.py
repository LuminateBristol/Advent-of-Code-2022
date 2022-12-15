"""
DAY 11: Monkey business

Challenge: https://adventofcode.com/2022/day/11
Input: https://adventofcode.com/2022/day/11/input

Notes:
    - Decided not to do any data parsing - naughty
    - Programming otherwise fairly straightforward
    - The downside of simple programming method is that it is very slow
    - It gets out of hand with data and so the 10000 round does not run fast enough for me to gather results :(
    - Need more efficient programming for that part!
"""
import operator
import numpy as np

def handledata():
    """
    I cheated on this one.
    I'm bored of parsing data every time so I've just written this one out manually.
    :return: dictionary of monkey data with: list of items held, operation, test with true and false monkey names
    """
    monkeys = {'monkey_0':[[83, 62, 93], [operator.mul, 17], [2, 'monkey_1', 'monkey_6'], 0],
               'monkey_1':[[90, 55], [operator.add, 1], [17, 'monkey_6', 'monkey_3'], 0],
               'monkey_2':[[91, 78, 80, 97, 79, 88], [operator.add, 3], [19, 'monkey_7', 'monkey_5'], 0],
               'monkey_3':[[64, 80, 83, 89, 59], [operator.add, 5], [3, 'monkey_7', 'monkey_2'], 0],
               'monkey_4':[[98, 92, 99, 51], [operator.mul, 'input'], [5, 'monkey_0', 'monkey_1'], 0],
               'monkey_5':[[68, 57, 95, 85, 98, 75, 98, 75], [operator.add, 2], [13, 'monkey_4', 'monkey_0'], 0],
               'monkey_6':[[74], [operator.add, 4], [7, 'monkey_3', 'monkey_2'], 0],
               'monkey_7':[[68, 64, 60, 68, 87, 80, 82], [operator.mul, 19], [11, 'monkey_4', 'monkey_5'], 0]
               }
    return monkeys

def handlethatmonkey(monkeys, monkeyname, worrydivider):
    '''
    Complete operations on each monkey to update the list
    Worry level is updated depending on monkey
    Return updated monkeys and number of inspections completed this round
    :param monkeys:
    :return: updated monkeys and total number of inspections
    '''
    inspected = 0
    for item in monkeys[monkeyname][0]:
        worry = 0
        # Step 1: Update worry of item based on operator
        if monkeys[monkeyname][1][1] == 'input': # Check for square condition
            worry = item * item
        else:
            worry = monkeys[monkeyname][1][0](item, monkeys[monkeyname][1][1]) # do operation from stored operator and corresponding int
        # Step 2: Monkey gets board: divide worry by 3 and round down
        worry = int(worry // worrydivider) # use int to round down
        # Step 3: Check division condition and throw the item to another monkey based on result
        if int(worry // monkeys[monkeyname][2][0]) == worry // monkeys[monkeyname][2][0]: # check if divisible
            monkeys[monkeys[monkeyname][2][1]][0].append(worry)
        else:
            monkeys[monkeys[monkeyname][2][2]][0].append(worry)
        inspected += 1
    monkeys[monkeyname][0].clear() # Clear list as all items have been thrown

    return monkeys, inspected


if __name__ == "__main__":
    # PART 1
    monkeys = handledata()

    rounds = 20
    for round in range(rounds):
        for monkeyname in monkeys:
            monkeys, inspected = handlethatmonkey(monkeys, monkeyname, 3)
            monkeys[monkeyname][3] += inspected

    totals = []
    for monkeyname in monkeys:
        totals.append(monkeys[monkeyname][3])
    print('The top two items of monkey business in Part 1 is: ', (sorted(totals)[-2:]))

    # PART 2
    # Added worry divider to function, this time it is set to 1 to represent no reduction in worry per round
    monkeys = handledata()

    rounds = 10000
    for round in range(rounds):
        print(round)
        for monkeyname in monkeys:
            monkeys, inspected = handlethatmonkey(monkeys, monkeyname, 1)
            monkeys[monkeyname][3] += inspected

    totals = []
    for monkeyname in monkeys:
        totals.append(monkeys[monkeyname][3])
    print('The top two items of monkey business in Part 2 is: ', (sorted(totals)[-2:]))
