from typing import *
from sys import maxsize

def valid_keys(keys_index: List[int], keys: List[str], required_state: str) -> bool:
    current_state = ['.'] * (len(required_state) - 2)
    for index in keys_index:
        # print(index, keys)
        key = keys[index]
        for btn in map(int,key[1:-1].split(',')):
            current_state[btn] = '#' if current_state[btn] == '.' else '.'
    # print(current_state, required_state)
    if "".join(current_state) == required_state[1:-1]:
        return True
    return False

def calculate_min_config(light_diagram: str, keys: List[str], joltage: str):
    # print(light_diagram, keys, joltage)
    min_keys = maxsize
    def recur(ind, picked_keys: List[int]):
        nonlocal min_keys
        if ind == len(keys):
            if valid_keys(picked_keys, keys, light_diagram) and len(picked_keys) < min_keys:
                min_keys = len(picked_keys)
            return
        recur(ind + 1, picked_keys + [ind])
        recur(ind + 1, picked_keys)
    recur(0,[])
    # print(min_keys)
    return min_keys

def sol1():
    with open("input.txt") as f:
        machines = f.read().splitlines()
        f.close()
    sum_min_keys = 0
    for machine in machines:
        machineList = machine.split(" ")
        light_diagram,keys,joltage = machineList[0], machineList[1:-1], machineList[-1]
        sum_min_keys += calculate_min_config(light_diagram, keys, joltage)
    print("Sum Min Keys",sum_min_keys)

sol1()

def calculate_min_config_with_joltage(light_diagram: str, keys: List[str], joltage: str):
    min_keys = maxsize


def sol2():
    with open("input.txt") as f:
        machines = f.read().splitlines()
        f.close()
    sum_min_keys = 0
    for machine in machines:
        machineList = machine.split(" ")
        light_diagram, keys, joltage = machineList[0], machineList[1:-1], machineList[-1]
        sum_min_keys += calculate_min_config_with_joltage(light_diagram, keys, joltage)
    print("Sum Min Keys", sum_min_keys)

sol2()