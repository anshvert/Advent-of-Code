from collections import deque

starting_x,starting_y,final_x,final_y = 1,1,31,39
fav_number = 1352
visited = {(starting_x,starting_y)}

Q = deque([(starting_x,starting_y,0)])
coordinates = [(0,1), (1,0), (0,-1), (-1,0)]
MAX_STEPS = 50

def count_bits(num):
    bits = 0
    while num:
        if num & 1:
            bits += 1
        num >>= 1
    return bits

def is_space(x,y):
    if x < 0 or y < 0:
        return False    
    val = x*x + 3*x + 2*x*y + y + y*y
    val += fav_number
    bits_count = count_bits(val)
    if bits_count & 1:
        return False
    return True

while Q:
    x,y,steps = Q.popleft()

    if steps + 1 <= MAX_STEPS:
        for dx,dy in coordinates:
            next_x,next_y = x + dx, y + dy
            if (next_x, next_y) not in visited and is_space(next_x,next_y):
                visited.add((next_x,next_y))
                Q.append((next_x,next_y,steps+1))

print("Unique locations", len(visited))