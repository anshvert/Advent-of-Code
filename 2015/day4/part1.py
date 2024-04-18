import hashlib

def md5Number(string,zeros):
    for i in range(1,10**7):
        newString = string + str(i)
        result = hashlib.md5(newString.encode()).hexdigest()
        if result[:zeros] == "0"*zeros:
            return i


Input = "ckczppom"
zeros = 5

print(md5Number(Input,zeros))