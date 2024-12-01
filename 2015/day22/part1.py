import heapq

# Define spells and their properties
spells = {
    "Magic Missile": {"cost": 53, "damage": 4, "heal": 0, "armor": 0, "turns": 0, "mana": 0},
    "Drain": {"cost": 73, "damage": 2, "heal": 2, "armor": 0, "turns": 0, "mana": 0},
    "Shield": {"cost": 113, "damage": 0, "heal": 0, "armor": 7, "turns": 6, "mana": 0},
    "Poison": {"cost": 173, "damage": 3, "heal": 0, "armor": 0, "turns": 6, "mana": 0},
    "Recharge": {"cost": 229, "damage": 0, "heal": 0, "armor": 0, "turns": 5, "mana": 101},
}

# Apply active effects
def apply_effects(player, boss, active_effects):
    for effect in list(active_effects.keys()):
        if active_effects[effect] > 0:
            if effect == "Poison":
                boss["hp"] -= spells[effect]["damage"]
            elif effect == "Recharge":
                player["mana"] += spells[effect]["mana"]
            elif effect == "Shield":
                player["armor"] = spells[effect]["armor"]
            active_effects[effect] -= 1
        if active_effects[effect] == 0 and effect == "Shield":
            player["armor"] = 0

# Simulate a turn
def simulate_turn(player, boss, active_effects, spell=None):
    apply_effects(player, boss, active_effects)

    if boss["hp"] <= 0:
        return player, boss, active_effects, True  # Boss defeated

    if spell:
        if spell in active_effects and active_effects[spell] > 0:
            return None  # Invalid move, effect already active
        if player["mana"] < spells[spell]["cost"]:
            return None  # Not enough mana
        player["mana"] -= spells[spell]["cost"]
        player["hp"] += spells[spell]["heal"]
        boss["hp"] -= spells[spell]["damage"]
        if spells[spell]["turns"] > 0:
            active_effects[spell] = spells[spell]["turns"]

    if boss["hp"] <= 0:
        return player, boss, active_effects, True  # Boss defeated

    # Boss turn
    apply_effects(player, boss, active_effects)

    if boss["hp"] <= 0:
        return player, boss, active_effects, True  # Boss defeated

    damage = max(1, boss["damage"] - player["armor"])
    player["hp"] -= damage

    if player["hp"] <= 0:
        return None  # Player defeated

    return player, boss, active_effects, False

# Solve using BFS
def solve(player, boss):
    initial_state = (0, player, boss, {}, False)  # (mana_spent, player, boss, active_effects, is_winner)
    queue = [initial_state]
    heapq.heapify(queue)
    min_mana_spent = float('inf')

    while queue:
        mana_spent, player, boss, active_effects, is_winner = heapq.heappop(queue)

        if is_winner:
            min_mana_spent = min(min_mana_spent, mana_spent)
            continue

        for spell in spells:
            new_player = player.copy()
            new_boss = boss.copy()
            new_effects = active_effects.copy()

            result = simulate_turn(new_player, new_boss, new_effects, spell)
            if result:
                new_player, new_boss, new_effects, winner = result
                new_mana_spent = mana_spent + spells[spell]["cost"]
                if new_mana_spent < min_mana_spent:
                    heapq.heappush(queue, (new_mana_spent, new_player, new_boss, new_effects, winner))

    return min_mana_spent

# Input
player = {"hp": 50, "mana": 500, "armor": 0}
boss = {"hp": 58, "damage": 9}  # Replace with your puzzle input

# Solve and output
min_mana_spent = solve(player, boss)
print("Minimum mana spent to win:", min_mana_spent)
