"""
--- Day 17: No Such Thing as Too Much ---
The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5
Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?

--- Part Two ---
While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is requesting as many containers as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you fill that number of containers and still hold exactly 150 litres?

In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be 3.
"""

ans = 0
minCount = float('inf')

def calculate(arr,val,ind,count):
    global ans,minCount
    if val < 0:
        return
    if ind == len(arr):
        if val == 0:
            if count < minCount:
                minCount = count
                ans = 1
            elif count == minCount:
                ans += 1
        return
    calculate(arr,val - arr[ind],ind+1, count + 1)
    calculate(arr,val,ind+1, count)

def TooMuch(fileInput):
    global ans
    containers = []
    for cons in fileInput:
        containers.append(int(cons))
    calculate(containers,150,0,0)
    return ans

with open("input.txt", "r") as file_input:
    print(TooMuch(file_input))