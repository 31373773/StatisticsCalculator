from StatisticFunctions.Covariance import Covariance
from StatisticFunctions.StandardDeviation import StandardDeviation


class PopulationCorrelation():
    @staticmethod

    def popCor(a, b):
        cov = Covariance.covariance(a, b)
        stdDevA = StandardDeviation.standardDeviation(a)
        stdDevB = StandardDeviation.standardDeviation(b)
        return cov/(stdDevA*stdDevB)