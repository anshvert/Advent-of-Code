from collections import Counter

filePath = "inputs/day7.txt"


def getHandRank(hand):
    count = Counter(hand)
    if len(count.keys()) == 1 and 5 in count.values():
        return 1
    elif len(count.keys()) == 2 and 4 in count.values():
        return 2
    elif len(count.keys()) == 2 and 3 in count.values():
        return 3
    elif len(count.keys()) == 3 and 3 in count.values():
        return 4
    elif len(count.keys()) == 3 and 2 in count.values():
        return 5
    elif len(count.keys()) == 4:
        return 6
    else:
        return 7


def getHandScore(hand):
    cardMap = {"A": 'a', "K": 'b', "Q": 'c', "J": 'd', "T": 'e', "9": 'f', "8": 'g', "7": 'h', "6": 'i', "5": 'j',
               "4": 'k', "3": 'l', "2": 'm'}
    handScore = ""
    for char in hand:
        handScore += cardMap[char]
    return handScore

def jokerizeHand(hand):
    if "J" in hand:
        count = Counter("".join([i for i in hand if i != "J"]))
        sortedItems = sorted(count.items(),key=lambda x: x[1],reverse=True)
        # if sortedItems[0][0] == sortedItems[1][0]:
        #     toBeReplaced =


def totalWinnings(inputFile):
    handScore, handRank,tsc = dict(), [],0
    for hand in inputFile:
        # print(hand)
        hand, score = hand.split(" ")
        updatedHand = jokerizeHand(hand)
        handScore[hand] = int(score.rstrip("\n"))
    #print(handScore)
    for hand in handScore.keys():
        handRank.append((hand, handScore[hand], getHandRank(hand), getHandScore(hand)))
    #print(handRank)
    handRank.sort(key=lambda x: [x[2], x[3]])
    print(handRank)
    for ind,val in enumerate(handRank):
        tsc += val[1]*(len(handRank)-ind)
    #return tsc

with open(filePath, "r") as file:
    print(totalWinnings(file))
