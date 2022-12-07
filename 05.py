"""
DAY 05: Find the stacked boxes
Challenge: https://adventofcode.com/2022/day/5
Input: https://adventofcode.com/2022/day/5/input

Notes:
    - took me ages to do all the parsing stuff but I think it should be fairly robust
    - will cause errors at the end if one stack is empty
    - PART 2 not correct - not sure why it isnt working!
"""

def handledata(inputdata):
    """
    Read the data from the text file and convert it into a list
    :return: sorted list
    """
    file = open(inputdata, "r").readlines()

    # Parse step 1: convert data into two sets, stacks and moves
    stackdata = []
    movedata = []
    index = 0
    for line in file:
        if index == 0:
            if line == '\n':
                index = 1
            else:
                stackdata.append(line)
        elif index == 1:
            movedata.append(line)

    # Parse step 2: convert stack data into a single list where each element is one vertical stack
    num_stacks = [int(x) for x in stackdata[len(stackdata)-1] if x.isdigit()]
    parsedstackdata = [[] for x in num_stacks]
    stackdata.pop()
    for line in stackdata:
        for i in range(len(num_stacks)):
            if list(line)[i*4+1] != ' ':
                parsedstackdata[i].append(list(line)[i*4+1])
    parsedstackdata = [elem[::-1] for elem in parsedstackdata]

    # Parse step 3: convert move data into digit form only
    parsedmovedata = []
    for i in movedata:
        parsedmovedata.append([int(x) for x in str.split(i) if x.isdigit()])
    return parsedstackdata, parsedmovedata

def moveboxes(stackdata, movedata):
    for i in range(len(movedata)):
        receivestack = movedata[i][2]-1
        givingstack = movedata[i][1]-1
        nummoves = movedata[i][0]
        for j in range(nummoves):
            stackdata[receivestack].append(stackdata[givingstack][len(stackdata[givingstack])-1])
            stackdata[givingstack].pop()
    return stackdata

def moveboxes9001(stackdata, movedata):
    for i in range(len(movedata)):
        receivestack = movedata[i][2]-1
        givingstack = movedata[i][1]-1
        nummoves = movedata[i][0]
        itemstomove = stackdata[givingstack][nummoves*-1:]
        for item in itemstomove:
            if item in itemstomove:
                stackdata[givingstack].remove(item)
                stackdata[receivestack].append(item)
    return stackdata


if __name__ == "__main__":
    # PART 1
    stackdata, movedata = handledata("Resources/05_a_input.txt")
    finalstackdata = moveboxes(stackdata, movedata)

    print("Top of stacks at the end of movements is:", ''.join([i[-1] for i in finalstackdata]))

    # PART 2
    stackdata, movedata = handledata("Resources/05_a_input.txt")
    finalstackdata = moveboxes9001(stackdata, movedata)

    print("Top of stacks at the end of 9001 super crane movements is:", ''.join([i[-1] for i in finalstackdata]))
