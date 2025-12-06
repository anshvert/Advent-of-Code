def isInvalidId(num):
    str_num = str(num)
    if str_num[:len(str_num) // 2] == str_num[len(str_num) // 2:]:
        return True
    return False

def isRepeating(num):
    if str(num) in (str(num) + str(num))[1:-1]:
        return True
    return False

def sol1():
    with open("input.txt") as f:
        lines = f.readlines()
        invalidIdsSum = 0
        for line in lines:
            ranges = line.split(",")
            for range_ in ranges:
                left,right = map(int,range_.split("-"))
                for num in range(left,right+1):
                    if isInvalidId(num):
                        invalidIdsSum += num
        print("InvalidId Sum 1", invalidIdsSum)

def sol2():
    with open("input.txt") as f:
        lines = f.readlines()
        invalidIdsSum = 0
        for line in lines:
            ranges = line.split(",")
            for range_ in ranges:
                left, right = map(int, range_.split("-"))
                for num in range(left, right + 1):
                    if isRepeating(num):
                        invalidIdsSum += num
        print("InvalidId Sum 2", invalidIdsSum)

sol1()
sol2()