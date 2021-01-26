import random as rng

grids = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], }
columns = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], }
rows = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], }

while len(grids[1]) != 9:
    number = rng.randint(0, 9)
    if number not in grids[1]:
        grids[1].append(number)
    else:
        number = rng.randint(0, 9)

print(grids[1])

for i in range(3):
    for j in range(0, 9, 3):
        columns[i + 1].append(grids[1][j + i])

for i in range(3):
    for j in range(3):
        rows[i+1].append(grids[1][j+(3*i)])

print(columns[1])
print(columns[2])
print(columns[3])

print(rows[1])
print(rows[2])
print(rows[3])
