import itertools
import math

original_puzzle = []

for i in range(9):
    row = input("Input Row: ")
    lst = row.split()
    int_lst = list(map(int, lst))
    original_puzzle.append(int_lst)

columns = list(itertools.zip_longest(*original_puzzle))
grids = [[], [], [], [], [], [], [], [], []]
blanks = {}
x_cord = 0
y_cord = 0
solved = False
cycles = 0


def init_grids():
    global grids
    grids = [[], [], [], [], [], [], [], [], []]
    for i in range(9):
        for j in range(3):
            for k in range(3):
                if i < 3:
                    grids[i].append(original_puzzle[j % 3][k + (i * 3)])
                elif i < 6:
                    grids[i].append(original_puzzle[(j % 3) + 3][(k + (i * 3)) - 9])
                else:
                    grids[i].append(original_puzzle[(j % 3) + 6][(k + (i * 3)) - 18])


def check_row(num, y):
    # print("Checking row", y, "for num", num)
    if num in original_puzzle[y]:
        return False
    else:
        return True


def check_column(num, x):
    # print("Checking column", x, "for num", num)
    if num in columns[x]:
        return False
    else:
        return True


def check_grid(num, y, x):
    grid_y = math.floor(y/3)
    grid_x = math.floor(x/3)
    # print("Checking grid", grid_x + (grid_y*3), "for num", num)
    if num in grids[grid_x + (grid_y*3)]:
        return False
    else:
        return True


def validity_check(num, y, x):
    if check_grid(num, y, x) and check_row(num, y) and check_column(num, x):
        return True
    else:
        return False


def find_empty(puzzle):
    empty_index = 0
    y = 0
    x = 0
    for row in puzzle:
        for cell in row:
            if cell == 0:
                blanks[empty_index] = [cell, y, x % 9]
                empty_index += 1
            x += 1
        y += 1


def blanks_to_puzzle(empty_cells):
    for i in empty_cells:
        original_puzzle[blanks[i][1]][blanks[i][2]] = blanks[i][0]


find_empty(original_puzzle)
init_grids()
index_blank = 0

while solved is False:
    blanks[index_blank][0] += 1
    if blanks[index_blank][0] == 10:
        blanks[index_blank][0] = 0
        index_blank -= 1
    if validity_check(blanks[index_blank][0], blanks[index_blank][1], blanks[index_blank][2]):
        index_blank += 1
    if index_blank == list(blanks.keys())[-1]+1:
        blanks_to_puzzle(blanks)
        print("DONE")
        break

    for r in original_puzzle:
        for c in r:
            print(c, end=" ")
        print()

    print("--------------------------")
    print("Cycles:", cycles)
    cycles += 1

    blanks_to_puzzle(blanks)
    init_grids()
    columns = list(itertools.zip_longest(*original_puzzle))

row = 0
column = 0
print("------+-------+--------")
for r in original_puzzle:
    for c in r:
        print(c, end=" ")
        column += 1
        if column % 3 == 0:
            print("|", end = " ")
    print()
    row += 1
    if row % 3 == 0:
        print("------+-------+--------")
