from numpy import absolute, asarray
from StatisticFunctions.Mean import mean
from MathOperations.root import Root

def standardDeviation(data):
   return Root.root((mean(absolute(asarray(data) - mean(data))**2)), 2)