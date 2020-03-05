from numpy import absolute, asarray
from StatisticFunctions.Mean import Mean

class Variance:
    @staticmethod
    def variance(data):
        return Mean.mean(absolute(asarray(data) - Mean.mean(data))**2)