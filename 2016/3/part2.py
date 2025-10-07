"""
--- Day 3: Squares With Three Sides ---
--- Part Two ---
Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically.
Each set of three numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603

In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?
"""

invalid_triangles,total_triangles = 0,0
s1_sides,s2_sides,s3_sides = [],[],[]

def check_invalid_triangle(s1,s2,s3):
    return s1 + s2 <= s3 or s2 + s3 <= s1 or s1 + s3 <= s2

with open("input.txt") as file:
    for triangle in file.read().splitlines():
        s1,s2,s3 = map(int,triangle.split())
        s1_sides.append(s1)
        s2_sides.append(s2)
        s3_sides.append(s3)

    file.close()


for side in [s1_sides,s2_sides,s3_sides]:
    for i in range(0,len(side),3):
        total_triangles += 1
        s1,s2,s3 = map(int,[side[i],side[i+1],side[i+2]])
        if check_invalid_triangle(s1,s2,s3):
            invalid_triangles += 1

print(total_triangles - invalid_triangles)