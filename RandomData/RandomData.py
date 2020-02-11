import random

def getRandomNums(seed, min, max, num):
    random.seed(seed)
    randomData = []
    i = 1
    while i < num + 1:
        randomData.append(random.randint(min, max))
        i += 1
    return randomData