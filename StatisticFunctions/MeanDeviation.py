from numpy import absolute, asarray
from StatisticFunctions.Mean import Mean

class MeanDeviation:
   @staticmethod
   def meanDeviation(data):
      return Mean.mean(absolute(asarray(data) - Mean.mean(data)))