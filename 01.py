"""
DAY 01: Find the elf with the most calories from a listed inventory
Challenge: https://adventofcode.com/2022/day/1
Input: https://adventofcode.com/2022/day/1/input

Notes:
    - Tried it with numpy but this requires you to know the size of the array so would need some pre-calcs
    - Defaulted to lists instead
"""

# PART 1:

file = open("Resources/01_a_input.txt", "r").read()
elf_inventory = [[]]
elf_inventory_totals = []
i = 0

for line in file.split('\n'):
    if line != '':
        elf_inventory[i].append(int(line))
    else:
        elf_inventory_totals.append(sum(elf_inventory[i]))
        i = i+1
        elf_inventory.append([])


maximum_inventory = max(elf_inventory_totals)
print(maximum_inventory)

# PART 2:

elf_inventory_totals.sort(reverse=True)

top_three_inventory = sum(elf_inventory_totals[:3])
print(top_three_inventory)