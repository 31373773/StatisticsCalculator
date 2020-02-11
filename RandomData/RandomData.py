from numpy.random import seed
from numpy.random import rand

def getRandomNums(seed, min, max, num):
    seed(seed)
    randomData = []
    i = 1
    while i < num + 1:
        randomData.append(rand(min, max))
        i += 1
    return randomData