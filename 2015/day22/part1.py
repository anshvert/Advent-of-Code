from copy import deepcopy


def solve_part1():
    # Initial values for Part 1
    playerHitPoints = 50
    playerMana = 500
    playerArmor = 0
    bossHitPoints = 58
    bossDamage = 9
    return find_min_mana(playerHitPoints, playerMana, playerArmor, bossHitPoints, bossDamage, hard_mode=False)


def solve_part2():
    # Initial values for Part 2
    playerHitPoints = 50
    playerMana = 500
    playerArmor = 0
    bossHitPoints = 58
    bossDamage = 9
    return find_min_mana(playerHitPoints, playerMana, playerArmor, bossHitPoints, bossDamage, hard_mode=True)


spells_data = {
    'magicMissile': {'cost': 53, 'damage': 4, 'heal': 0, 'armor': 0, 'mana': 0, 'turns': 0},
    'drain': {'cost': 73, 'damage': 2, 'heal': 2, 'armor': 0, 'mana': 0, 'turns': 0},
    'shield': {'cost': 113, 'damage': 0, 'heal': 0, 'armor': 7, 'mana': 0, 'turns': 6},
    'poison': {'cost': 173, 'damage': 3, 'heal': 0, 'armor': 0, 'mana': 0, 'turns': 6},
    'recharge': {'cost': 229, 'damage': 0, 'heal': 0, 'armor': 0, 'mana': 101, 'turns': 5}
}


def find_min_mana(playerHP, playerMana, playerArmor, bossHP, bossDamage, hard_mode):
    min_mana_spent = float('inf')

    # State: (playerHP, playerMana, currentArmor, bossHP, manaSpent, activeSpells)
    # currentArmor is the *effective* armor for the current turn, which will be reset after boss attack.
    # The actual armor state is managed by the 'shield' spell in activeSpells.
    queue = [(playerHP, playerMana, playerArmor, bossHP, 0,
              {})]  # (hp, mana, armor_buff, boss_hp, mana_spent, active_spells)

    while queue:
        current_player_hp, current_player_mana, current_player_armor, current_boss_hp, current_mana_spent, active_spells = queue.pop(
            0)

        # Player's Turn
        # 1. Hard Mode: Player loses 1 HP
        if hard_mode:
            current_player_hp -= 1
            if current_player_hp <= 0:
                continue  # Player died

        # 2. Apply spell effects
        temp_player_armor = 0  # Armor is temporary for the current turn
        new_active_spells = deepcopy(active_spells)
        spells_to_remove = []

        for spell_name, spell_info in new_active_spells.items():
            if spell_name == 'shield':
                temp_player_armor = spells_data['shield']['armor']  # Apply shield armor
            elif spell_name == 'poison':
                current_boss_hp -= spells_data['poison']['damage']
            elif spell_name == 'recharge':
                current_player_mana += spells_data['recharge']['mana']

            new_active_spells[spell_name]['turns'] -= 1
            if new_active_spells[spell_name]['turns'] == 0:
                spells_to_remove.append(spell_name)

        for spell_name in spells_to_remove:
            del new_active_spells[spell_name]

        # 3. Check if boss is defeated after effects
        if current_boss_hp <= 0:
            min_mana_spent = min(min_mana_spent, current_mana_spent)
            continue  # This path resulted in a win

        # 4. Player casts a spell
        for spell_name, spell_info in spells_data.items():
            cost = spell_info['cost']

            if current_player_mana >= cost:
                # Cannot cast if already active and it's a persistent spell
                if spell_name in ['shield', 'poison', 'recharge'] and spell_name in new_active_spells:
                    continue

                new_mana_spent = current_mana_spent + cost
                if new_mana_spent >= min_mana_spent:  # Pruning
                    continue

                next_player_hp = current_player_hp
                next_player_mana = current_player_mana - cost
                next_boss_hp = current_boss_hp
                next_active_spells = deepcopy(new_active_spells)

                if spell_name == 'magicMissile':
                    next_boss_hp -= spell_info['damage']
                elif spell_name == 'drain':
                    next_boss_hp -= spell_info['damage']
                    next_player_hp += spell_info['heal']
                else:  # Persistent spells
                    next_active_spells[spell_name] = {'turns': spell_info['turns']}

                # Check if boss is defeated immediately after player casts
                if next_boss_hp <= 0:
                    min_mana_spent = min(min_mana_spent, new_mana_spent)
                    continue

                # Boss's Turn (after player's action)
                # Apply spell effects again for boss's turn
                boss_turn_active_spells = deepcopy(next_active_spells)
                boss_turn_boss_hp = next_boss_hp
                boss_turn_player_mana = next_player_mana
                boss_turn_player_armor = 0  # Reset armor for boss turn and recalculate from shield

                boss_spells_to_remove = []
                for s_name, s_info in boss_turn_active_spells.items():
                    if s_name == 'shield':
                        boss_turn_player_armor = spells_data['shield']['armor']  # Apply shield armor
                    elif s_name == 'poison':
                        boss_turn_boss_hp -= spells_data['poison']['damage']
                    elif s_name == 'recharge':
                        boss_turn_player_mana += spells_data['recharge']['mana']

                    boss_turn_active_spells[s_name]['turns'] -= 1
                    if boss_turn_active_spells[s_name]['turns'] == 0:
                        boss_spells_to_remove.append(s_name)

                for s_name in boss_spells_to_remove:
                    del boss_turn_active_spells[s_name]

                # Check if boss is defeated after effects on their turn
                if boss_turn_boss_hp <= 0:
                    min_mana_spent = min(min_mana_spent, new_mana_spent)
                    continue

                # Boss attacks
                damage_taken = max(1, bossDamage - boss_turn_player_armor)
                final_player_hp = next_player_hp - damage_taken

                if final_player_hp > 0:
                    # Add to queue for next player turn
                    queue.append((final_player_hp, boss_turn_player_mana, boss_turn_player_armor, boss_turn_boss_hp,
                                  new_mana_spent, boss_turn_active_spells))

    return min_mana_spent


print("Part 1 Min Mana Spent:", solve_part1())
print("Part 2 Min Mana Spent (Hard Mode):", solve_part2())