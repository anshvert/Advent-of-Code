from typing import *

def count_adjacent_rolls(mat: Union[List[List[str]], List[str]], i: int, j: int) -> int:
    dirs = [(0,1),(0,-1),(-1,0),(1,0), (1,1), (-1,-1),(-1,1), (1,-1)]
    count = 0
    for dx,dy in dirs:
        if 0 <= i + dx < len(mat) and 0 <= j + dy < len(mat):
            if mat[i + dx][j + dy] == '@':
                count += 1
    return count

def sol1() -> None:
    with open("input.txt") as f:
        lines = f.read().splitlines()
        ans = 0
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == "@":
                    if count_adjacent_rolls(lines,i,j) <= 3:
                        ans += 1
        print('Final Roll Count:', ans)

def sol2() -> None:
    rollMat = []
    with open("input.txt") as f:
        rollMat = f.read().splitlines()
        rollMat = [list(line) for line in rollMat]
        f.close()

    ans = 0
    while 1:
        can_remove_rolls = []
        for i in range(len(rollMat)):
            for j in range(len(rollMat[i])):
                if rollMat[i][j] == "@":
                    if count_adjacent_rolls(rollMat, i, j) <= 3:
                        ans += 1
                        can_remove_rolls.append((i,j))

        for x, y in can_remove_rolls:
            rollMat[x][y] = '.'
        if not can_remove_rolls:
            break

    print('Total Rolls Removed', ans)

sol1()
sol2()