from numpy import absolute, asarray
from StatisticFunctions.Mean import mean

def meanDeviation(data):
   return mean(absolute(asarray(data) - mean(data)))