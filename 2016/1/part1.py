"""
--- Day 1: No Time for a Taxicab ---
Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.
How many blocks away is Easter Bunny HQ?

Your puzzle answer was 353.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?
"""

# Shitty Code Warning !!!!

with open("input.txt") as file:
    steps_str,x,y,current_dir = "",0,0,"N"

    for steps in file:
        steps_str += steps
    steps_arr = steps_str.split(",")
    cache_steps = set()
    for steps in steps_arr:
        steps = steps.strip()
        direction, step_count = steps[0], int(steps[1:])
        if direction == "R":
            if current_dir == "N":
                while step_count:
                    x += 1
                    if (x,y) in cache_steps:
                        print(x + y)
                        break
                    cache_steps.add((x,y))
                    step_count -= 1
                current_dir = "E"
            elif current_dir == 'E':
                while step_count:
                    y -= 1
                    if (x,y) in cache_steps:
                        print(x + y)
                        break
                    cache_steps.add((x,y))
                    step_count -= 1
                current_dir = "S"
            elif current_dir == "S":
                while step_count:
                    x -= 1
                    if (x,y) in cache_steps:
                        print(x + y)
                        break
                    cache_steps.add((x,y))
                    step_count -= 1
                current_dir = "W"
            else:
                while step_count:
                    y += 1
                    if (x,y) in cache_steps:
                        print(x + y)
                        break
                    cache_steps.add((x,y))
                    step_count -= 1
                current_dir = "N"
        elif direction == "L":
            if current_dir == "W":
                while step_count:
                    y -= 1
                    if (x,y) in cache_steps:
                        print(x + y)
                        break
                    cache_steps.add((x,y))
                    step_count -= 1
                current_dir = "S"
            elif current_dir == 'S':
                while step_count:
                    x += 1
                    if (x,y) in cache_steps:
                        print(x + y)
                        break
                    cache_steps.add((x,y))
                    step_count -= 1
                current_dir = "E"
            elif current_dir == 'E':
                while step_count:
                    y += 1
                    if (x,y) in cache_steps:
                        print(x + y)
                        break
                    cache_steps.add((x,y))
                    step_count -= 1
                current_dir = "N"
            else:
                while step_count:
                    x -= 1
                    if (x,y) in cache_steps:
                        print(x + y)
                        break
                    cache_steps.add((x,y))
                    step_count -= 1
                current_dir = "W"