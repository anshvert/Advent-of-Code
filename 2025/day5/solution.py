def sol1()-> None:
    with open('input.txt') as f:
        lines = f.read().splitlines()
        queryIndex = lines.index("")
        ranges, queries = lines[:queryIndex], lines[queryIndex+1:]
        f.close()

    fresh_count = 0
    for q in queries:
        for r in ranges:
            left,right = r.split("-")
            if int(left) <= int(q) <= int(right):
                fresh_count += 1
                break
    print('Fresh Count:', fresh_count)

def sol2() -> None:
    with open('input.txt') as f:
        lines = f.read().splitlines()
        queryIndex = lines.index("")
        ranges = lines[:queryIndex]
        f.close()

    ranges = sorted([(int(x),int(y)) for x,y in (i.split("-") for i in ranges)])
    current_fresh_Ids,rInd = 0,0
    while rInd < len(ranges):
        crInd,maxRight = rInd,ranges[rInd][1]
        while crInd + 1 < len(ranges) and ranges[crInd + 1][0] <= ranges[crInd][1]:
            maxRight = max(maxRight, ranges[crInd+1][1])
            crInd += 1
        current_fresh_Ids += (maxRight - ranges[rInd][0]) + 1
        rInd = crInd + 1
    print('Current Fresh Ids:', current_fresh_Ids)

sol1()
sol2()