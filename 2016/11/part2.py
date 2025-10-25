from collections import deque
from itertools import combinations

def is_safe(materials):
    gens,chips = set(),set()

    for material in materials:
        if material[-1] == 'M':
            chips.add(material)
        else:
            gens.add(material)

    if not len(gens):
        return True

    for chip in chips:
        if chip[:-1] + "G" not in gens:
            return False
    return True

initial_floor_items = [
    ['PG', 'PM', 'EG', 'EM', 'DG', 'DM'],
    ['CBG', 'CG', 'RG', 'PTG'],
    ['CBM', 'CM', 'RM', 'PTM'],
    []
]

initial_state_tuple = (
    0,
    tuple(frozenset(val) for val in initial_floor_items)
)

Q = deque([(initial_state_tuple, 0)])
cache = {initial_state_tuple}

TOTAL_ITEMS = sum(len(f) for f in initial_floor_items)
MAX_FLOOR_INDEX = 3

while Q:
    (floor, floor_state), steps = Q.popleft()

    if len(floor_state[MAX_FLOOR_INDEX]) == TOTAL_ITEMS:
        print("Minimum steps taken:", steps)
        break

    current_floor_items = floor_state[floor]

    if not current_floor_items and floor != MAX_FLOOR_INDEX:
        continue

    moves_of_one = list(combinations(current_floor_items, 1))
    moves_of_two = list(combinations(current_floor_items, 2))
    all_possible_moves = moves_of_one + moves_of_two

    possible_destinations = []
    if floor < MAX_FLOOR_INDEX:
        possible_destinations.append(floor + 1)
    if floor > 0:
        possible_destinations.append(floor - 1)

    for move in all_possible_moves:
        for next_floor in possible_destinations:
            if next_floor < floor and all(len(floor_state[i]) == 0 for i in range(floor)):
                continue

            new_floor_contents_list = list(list(f) for f in floor_state)
            for item in move:
                new_floor_contents_list[floor].remove(item)

            new_floor_contents_list[next_floor].extend(move)

            if not is_safe(new_floor_contents_list[floor]) or not is_safe(new_floor_contents_list[next_floor]):
                continue

            new_floor_state_tuple = tuple(frozenset(f) for f in new_floor_contents_list)
            new_state = (next_floor, new_floor_state_tuple)

            if new_state not in cache:
                cache.add(new_state)
                Q.append((new_state, steps + 1))