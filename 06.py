"""
DAY 06: Find the location of the packet header from a looooon string
Challenge: https://adventofcode.com/2022/day/6
Input: https://adventofcode.com/2022/day/6/input

Notes:
    -
"""

def handledata(inputdata):
    """
    Read the data from the text file - single string in this case
    :return: string from input
    """
    file = open(inputdata, "r").read()
    return file

def findstartnum(packetstring, n):
    """
    Finds the character number that represents the packet start character
    This is the first character that is unique when compared to the three previous characters
    e.g. in jdjdjklidis character 7 where l is the start letter with djk the preceding three characters
    :param packetstring: string input
    :param n: the number of unique characters prior to the start character
    :return: character number for start of packet
    """
    for i in range(len(packetstring)):
        if i > n-1:
            teststring = packetstring[i-n:i]
            if len(set(teststring)) == len(teststring): # set(x) just takes all characters that are unique and so len will only be equal (TRUE) if there are no repeated characters
                return i

if __name__ == "__main__":
    # PART 1
    packet = handledata("Resources/06_a_input.txt")
    print("Packet start is at character number for n = 4: ", findstartnum(packet, 4))

    # PART 2
    print("Packet start is at character number for n = 14: ", findstartnum(packet, 14))
