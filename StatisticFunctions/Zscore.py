from StatisticFunctions.StandardDeviation import StandardDeviation
from StatisticFunctions.Mean import Mean
from RandomGenerator.PickSeedList import PickSeedList
from numpy import asarray


class Zscore():
    @staticmethod

    def zscore(sd, data):
        x = PickSeedList.pickSeed(sd, data)
        mn = Mean.mean(data)
        stdDev = StandardDeviation.standardDeviation(data)
        return (x-mn)/(stdDev)