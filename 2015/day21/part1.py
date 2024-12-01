from itertools import combinations
from math import ceil

weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
armors = [(0, 0, 0)] + [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
rings = [(0, 0, 0)] + [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

ring_combinations = []
for i in range(3):  # 0, 1, or 2 rings
    ring_combinations += combinations(rings, i)

enemy_health = 109
enemy_attack = 8
enemy_armor = 2
min_cost = float('inf')

def wins(hp1, atk1, arm1, hp2, atk2, arm2):
    A1 = max(1, atk1 - arm2)
    A2 = max(1, atk2 - arm1)
    return ceil(hp2 / A1) <= ceil(hp1 / A2)

for weapon in weapons:
    for arm in armors:
        for ring_set in ring_combinations:
            total_cost = weapon[0] + arm[0] + sum(r[0] for r in ring_set)
            total_attack = weapon[1] + arm[1] + sum(r[1] for r in ring_set)
            total_armor = weapon[2] + arm[2] + sum(r[2] for r in ring_set)

            if wins(100, total_attack, total_armor, enemy_health, enemy_attack, enemy_armor):
                min_cost = min(min_cost, total_cost)

print(min_cost)
