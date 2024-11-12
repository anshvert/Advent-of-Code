"""
--- Day 18: Like a GIF For Your Yard ---
After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights, he says, you'll have to resort to animation.

Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:

1B5...
234...
......
..123.
..8A4.
..765.
The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
All of the lights update simultaneously; they all consider the same current state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......
After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?


"""

import copy

steps = 1

def countOn(grid):
    count = 0
    for i in grid:
        count += i.count('#')
    return count

def getNStats(grid,i,j):
    on,off = 0,0
    dirs = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
    for x,y in dirs:
        if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]):
            if grid[i+x] == ".":
                off += 1
            else:
                on += 1

    return on,off

def printGrid(grid):
    for i in grid:
        print(i)

def animate(grid, cSteps):
    global steps
    if cSteps == steps:
        printGrid(grid)
        print("Total Steps", steps)
        return countOn(grid)

    aGrid = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(i+1,len(grid[0])):
            on,off = getNStats(grid,i,j)
            if grid[i][j] == ".":
                if on == 3:
                    aGrid[i][j] = '#'
            else:
                if on not in [2,3]:
                    aGrid[i][j] = "."

    return animate(aGrid, cSteps+1)

def GIF(fileInput):
    grid = []
    for row in fileInput:
        grid.append(list(row.rstrip()))
    return animate(grid,0)

with open("./input.txt", "r") as file_input:
    print(GIF(file_input))