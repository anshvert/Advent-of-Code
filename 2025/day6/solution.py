from collections import defaultdict
from operator import mul,add
from functools import reduce

def sol1():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        operations = defaultdict(list)
        for line in lines:
            for ind, val in enumerate(line.strip().split()):
                operations[ind].append(val)
        grand_total = 0
        for values in operations.values():
            if values[-1] == '+':
                grand_total += sum(map(int,values[:-1]))
            elif values[-1] == '*':
                grand_total += reduce(mul, map(int,values[:-1]))
        print("Grand Total:", grand_total)

def sol2():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        ops,operators = [],lines[-1].split()[::-1]
        for col_ind in range(len(lines[0])-1,-1,-1):
            current_column_string = ""
            for row_ind in range(len(lines)-1):
                if lines[row_ind][col_ind] != '':
                    current_column_string += lines[row_ind][col_ind]
            ops.append(current_column_string)
        cl,temp_numbers = 0,[]
        grand_total = 0
        while ops or temp_numbers:
            current_num = ops.pop().replace('x','').strip() if ops else ""
            if current_num != "":
                temp_numbers.append(int(current_num))
            else:
                operator = operators.pop()
                if operator == '*':
                    grand_total += reduce(mul, temp_numbers)
                elif operator == '+':
                    grand_total += reduce(add, temp_numbers)
                temp_numbers = []
        print("Grand Total:", grand_total)

sol1()
sol2()
