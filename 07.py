"""
DAY 07: Find the total directory sizes from a computer filing system

Challenge: https://adventofcode.com/2022/day/7
Input: https://adventofcode.com/2022/day/7/input

Notes:
    - not managed this one yet!
    - so far I have built some classes to allow for a tree structure to be built
    - now need to work out how to parse data into this structure
    - then need to manipulate that data so that we can work out the size of each directory
"""

def handledata(inputdata):
    """
    Read the data from the text file - single string in this case
    :return: string from input
    """
    file = open(inputdata, "r").readlines()
    return file

class Tree:
    def __init__(self, root):
        self.root = root
        self.children = {}

    def addDir(self, dir):
        self.children[dir] = {}

    def addFile(self, file, size):
        self.children.update({file: size})

class Node():
    def __init__(self, data):
        self.data = data
        self.children = {}

    def addDir(self, obj):
        self.children[dir] = {}

    def addFile(self, file, size):
        self.children.update({file: size})

def parsetotree(terminaldata):
    locator = '/'



if __name__ == "__main__":
    # Testing the tree idea
    root = Tree('/')
    root.addDir(Node('bsnqsfm'))
    root.addDir(Node('dtqvbspj'))
    root.addFile('pnm.slh', 307337)

    print(root.children)


    # cd a folder - we need to update the current directory to the new one

    command = 'cd'
    locator = 'bsnqsfm'
    current_dir = root.children # TODO: how can I update the current directory using dicts of dicts?
    # we are currently in / but want to go into bsnqsfm to add stuff
    if command == 'cd':
        # Find the index of the current dictionary to edit
        for x in current_dir:
            if not isinstance(x, str):
                if x.data == locator:
                    index = list(current_dir).index(x)

        current_dir = root.children[index]
        print(current_dir)







    # PART 1
    commands = handledata("Resources/07_a_input.txt")

