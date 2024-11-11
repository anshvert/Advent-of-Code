"""
--- Day 17: No Such Thing as Too Much ---
The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5
Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?
"""

ans = 0

def calculate(arr,val,ind):
    global ans
    if val < 0:
        return
    if ind == len(arr):
        if val == 0:
            ans += 1
        return
    calculate(arr,val - arr[ind],ind+1)
    calculate(arr,val,ind+1)

def TooMuch(fileInput):
    global ans
    containers = []
    for cons in fileInput:
        containers.append(int(cons))
    calculate(containers,150,0)
    return ans

with open("input.txt", "r") as file_input:
    print(TooMuch(file_input))