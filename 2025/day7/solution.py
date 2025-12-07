def sol1():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        laser_columns,split_count = set(),0
        for line in lines:
            for ind,char in enumerate(line):
                if char == "S":
                    laser_columns.add(ind)
                elif char == '^':
                    if ind in laser_columns:
                        laser_columns.remove(ind)
                        laser_columns.add(ind+1)
                        laser_columns.add(ind-1)
                        split_count += 1
        print("Split Count", split_count)

def sol2():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        manifold = [list(i) for i in lines]
        for i in range(len(manifold)):
            for j in range(len(manifold[i])):
                if manifold[i][j] == 'S':
                    manifold[i][j] = 1
                elif manifold[i][j] == '.':
                    manifold[i][j] = manifold[i-1][j] if (i-1 >= 0 and manifold[i-1][j] != '^') else 0
                elif manifold[i][j] == '^':
                    manifold[i][j-1] += manifold[i-1][j]
                    manifold[i][j+1] = manifold[i-1][j]
                else:
                    manifold[i][j] += manifold[i-1][j]
        print("Total Timelines", sum(manifold[-1]))

sol1()
sol2()