
Connor Letko
Stephanie Velez

Calculator Object
Properties
Result 
Methods
Addition -> Calls addition static method from math operations
Subtraction -> Call subtraction static method from Math operations
Multiplication -> Call multiplication static method from Math operations
Division -> Call multiplication static method from Math operations
Exponentiation -> Call exponentiation static method from Math operations
Root -> Call root static method from Math operations
Logarithm -> Call log static method from Math operations
Math Operations Static Class(s)
Addition
Methods 
Sum 1 numbers
Sum List of numbers
Subtraction
Methods
Subtract 2 numbers
Multiplication
Methods
Multiply 2 numbers
Division
Methods
Divide 2 numbers
Exponentiation
Methods
Raise first variable to the power of the second variable
Root
Methods
Take the nth root of the first variable using second variable
Logarithm
Methods
Take the nth log of a number
Statistics Calculator Object
Properties
Result
Methods
Mean -> Call mean static method from Descriptive Statistics
Median -> Call median static method from Descriptive Statistics
Mode -> Call mode static method from Descriptive Statistics
Variance -> Call variance static method from Descriptive Statistics
Standard Deviation -> Call standard deviation static method from Descriptive Statistics
Quartiles -> Call quartiles static method from Descriptive Statistics
Skewness -> Call skewness static method from Descriptive Statistics
Population Correlation -> Call population correlation static method from Descriptive Statistics
Sample Correlation -> Call sample correlation static method from Descriptive Statistics
Z-Score -> Call z-score static method from Descriptive Statistics
Mean Deviation -> Call meanDeviation static method from Descriptive Statistics
GenerateNumNoSeed -> Call generateNum static method from Random Generator Function
GenerateNumSeed -> Call generateNumSeed static method from Random Generator Function
GenerateList -> Call generateListstatic method from Random Generator Function
SelectFromList -> Call selectItem static method from Random Generator Function
SetAndSelectSeed -> Call setSeed static method from Random Generator Function
SelectItemsNoSeed -> Call selectItem static method from Random Generator Function
SelectItemsSeed -> Call selectItemSeedstatic method from Random Generator Function
SimpleRandomSampling -> Call simpleSampling static method from Population Sampling
SystematicSampling -> Call systematicSampling static method from Population Sampling
ConfidenceInterval -> Call conf static method from Population Sampling
MarginError -> Call marginErrorstatic method from Population Sampling
FindConfidenceInterval -> Call findConf static method from Population Sampling
Cochran -> Call cochran static method from Population Sampling
SampleSizeUnknown -> Call findSample static method from Population Sampling
SampleSizeKnown -> Call findSampleKnown static method from Population Sampling
Descriptive Statistics Functions Static Class(s)
Mean
Methods
Call addition static method and division static method from MathOperations
Median
Methods
Call addition static method and division static method from MathOperations
Mode
Methods
Call max python function and count
Variance
Methods
Call Mean from StatisticFunctions
StandardDeviation
Methods
Call Variance from StatisticFunctions
Quartiles
Methods
Import numpy, set variables A, B, C to  numpy.quantile -> takes in data and quantile (.25, .5, or .75)
Skewness
Methods
Import scipy.stats use .skew -> takes in data
PopulationCorrelation
Methods
Call Covariance and StandardDeviation  from StatisticalFunctions.
Takes in a, b
stdDevA and stdDevB convert a and b into the standard deviation of each
 Covariance(a,b) divided by stdDevA*stdDevB
SampleCorrelation
Methods
Call Covariance and StandardDeviation  from StatisticalFunctions, call SelectWithSeed from RandomGenerator
Random Generator Function Static Class(s)
GenerateNumNoSeed
Methods
Calls randint, and uniform from random
GenerateNumSeed
Methods
Calls seed, randint, and uniform from random
GenerateList
Methods
  Calls seed, randint, and uniform from random
SelectFromList
Methods
 Call randint from numpy
Picks item in list, returns the item
SetAndSelectSeed
Methods
 Calls seed from numpy
SelectItemsNoSeed
Methods
Calls randint from random
Returns lst2 -> Items in list without seed
SelectItemsSeed
Methods
Calls SelectWithoutSeed from RandomGenerator 
Returns lst2 -> Items in list with seed
Population Sampling Function Static Class(s)
SimpleRandomSampling
Methods
 Calls Exponentiation from MathOperations
Calls PopulationProportion and Zscore from StatisticsFunctions 
Calls MarginError from PopulationSamplingFunctions
SystematicSampling
Methods
 Calls RandomWithSeeds fromRandomGenerator
ConfidenceInterval
Methods
Calls sem and t from stats
Calls Mean from StatisticsFunctions
MarginError
Methods
 Calls StandardDeviation static method and Zscore static method from StatisticFunctions
FindConfidenceInterval
Methods
Calls sem and t from stats
Cochran
Methods
 Calls PopulationProportion static method and Zscore static method from StatisticFunctions
Calls MarginError static method from PopulationSamplingFunctions
Calls Exponentiation from MathOperations
SampleSizeUnknown
Methods
Calls  Zscore static method from StatisticFunctions
Calls MarginError static method from PopulationSamplingFunctions
Calls Exponentiation from MathOperations
SampleSizeKnown
Methods
Calls  Zscore static method and StandardDeviation static method from StatisticFunctions
Calls MarginError static method from PopulationSamplingFunctions
Calls Exponentiation from MathOperations
Task 1: Create Calculator
User Story: Developer wants to create a calculator object
Steps: Create calculator directory and calculator.py, create a calculator class with a calculator object.
Expected Results: Create and instance of a calculator

Task 3: Addition Function
User Story: Developer wants to calculate the sum of 2 numbers, or a list of numbers
Formula Steps: a+b = c, a+b+c+d+... = z
Example data: 1,2 and [1,2,3,4]
Expected Results: 3 and 10

Task 5: Subtraction Function
User Story: Developer wants to calculate the difference between 2 numbers
Formula Steps: a-b=c
Example Data:2,1
Expected Result: 1

Task 6: Multiplication Function 
User Story: Developer wants to multiply two numbers together
Formula Steps: a*b=c
Example Data: 3,2
Expected Result: 6

Task 7: Division Function
User Story: Developer wants to divide two numbers
Formula Steps: a/b=c
Example Data: 10,5
Expected Result: 2

Task 8: Exponentiation Function
User Story: Developer wants to raise a number to the nth power
Formula Steps: x^n
Example Data: 2,3
Expected Result: 8

Task 9: Nth Root Function
User Story: Developer wants to calculate the nth root of a number
Formula Steps: Exponentiation, (1/root)
Example Data: 4,2
Expected Result: 2

Task 10: Logarithm Function
User Story: Developer wants to calculate the log of a number
Formula Steps: math.log, math.log10
Example Data: 10, 100
Expected Result: 2

Task 11: Statistics Calculator
User Story: Developer wants to create a statistics calculator object
Formula Steps: Calculator
Example Data: 
Expected Result: Statistics Calculator 

Task 12: Mean Function
User Story: Developer wants to calculate the Mean of a data set
Formula Steps: sum, count, divide
Example Data: 1,2,3,4
Expected Result: 2.5

Task 13: Median Function
User Story: Developer wants to calculate the Median of a data set
Formula Steps: len, sorted, sum
Example Data: 1,2,3,4
Expected Result: 2.5

Task 14: Mode Function
User Story: Developer wants to calculate the Mode of a data set
Formula Steps: max, set, count
Example Data: 1,2,2,3,4
Expected Result: 2

Task 15: Variance Function
User Story: Developer wants to calculate the Variance of a data set
Formula Steps: Mean, for loop, division
Example Data: 1,2,3,4
Expected Result: 1.25

Task 16: Standard Deviation Function
User Story: Developer wants to calculate  the Standard Deviation of a data set
Formula Steps: Variance, Square Root
Example Data: 1,2,3,4
Expected Result: 1.1180339887499

Task 17: Quartiles Function
User Story: Developer wants to calculate the quartiles of a data set
Formula Steps: numpy.quantile
Example Data: 1,2,3,4
Expected Result: [1.25, 2.5, 3.5]

Task 18: Skewness Function
User Story: Developer wants to calculate the skewness of a data set
Formula Steps: Mean, Median, Division, Standard Deviation
Example Data: 1,2,3,4
Expected Result: 

Task 19: Covariance Function
User Story: Developer wants to calculate the covariance of a data set
Formula Steps: numpy.cov
Example Data: 1,2,3,4
Expected Result: 

Task 20: Population Correlation Function
User Story: Developer wants to calculate the population correlation of a data set
Formula Steps: Covariance, Standard Deviation, Division
Example Data: 1,2,3,4
Expected Result: 

Task 21: Mean Deviation / Mean Absolute Deviation Function
User Story: Developer wants to calculate the mean absolute deviation of a data set
Formula Steps: Mean, Sum, Count, Division
Example Data: 1,2,3,4
Expected Result: 

Task 22: Generate Random Number No Seed Integer Function
User Story: Developer wants to generate a random integer with no seed
Formula Steps: numpy.randInt
Example Data: 0, 10
Expected Result: is an Int

Task 23: Generate Random Number No Seed Decimal Function
User Story: Developer wants to generate a random float with no seed
Formula Steps: numpy.uniform
Example Data: 0. 10
Expected Result: is a float

Task 24: Generate Random Number With Seed Integer Function
User Story: Developer wants to generate a random integer with a seed
Formula Steps: seed, numpy.randInt
Example Data: seed = 4, 0, 10
Expected Result: same value when called twice

Task 25: Generate Random Number With Seed Decimal Function
User Story: Developer wants to generate a random float with a seed
Formula Steps: seed, numpy.uniform
Example Data: seed = 4, 0, 10
Expected Result: same value when called twice

Task 26: Generate A List Of N Numbers Integer Function
User Story: Developer wants to generate a list of random integers
Formula Steps: numpy.seed, randint, append
Example Data: 0, 10, 5, 4
Expected Result: [7,5,1,8,7]

Task 27: Generate A List Of N Numbers Decimal Function
User Story: Developer wants to generate a list of random floats
Formula Steps: numpy.seed, uniform, append
Example Data:0, 10, 5, 4
Expected Result: [9.670, 5.472, 9.726, 7.148, 6.977]

Task 28: Select Random Item From List Function
User Story: Developer wants to select a random item from a list
Formula Steps: len, numpy.randInt
Example Data: 0, 10, 5, 4
Expected Result: 7

Task 29: Select Seed and Get it From List Function
User Story: Developer wants to set a seed and select the same item from the list every time
Formula Steps: seed, SelectItemList
Example Data: 0, 10, 5, 4
Expected Result: 1

Task 30: Select N Items From List No Seed Function
User Story: Developer wants to select N number of items from a list with no seed set
Formula Steps: len, randInt, append
Example Data: 0, 10, 5, 4
Expected Result: 

Task 31: Select N Items From List With Seed Function
User Story: Developer wants to select N number of items from a list with a seed set
Formula Steps: seed, len, randInt, append
Example Data: 0, 10, 5, 4
Expected Result: 

Task 32: Sample Correlation Function
User Story: Developer wants to calculate the sample correlation of a data set
Formula Steps: select with seed, covariance, standard deviation
Example Data:
Expected Result: 

Task 33: Z-Score Function
User Story: Developer wants to calculate the Z score of a specific item in a data set
Formula Steps: Set and select seed, mean, standard deviation, divide
Example Data: 1, 2, 3, 4
Expected Result: 

Task 34: Simple Random Sampling Function
User Story: Developer wants to calculate random sample that is a subset of a larger set
Formula Steps: Select with seed, list, range
Example Data:
Expected Result: 

Task 35: Systematic Sampling Function
User Story: Developer wants to calculate which sample members from a larger population are selected according to a random starting point but with a fixed, periodic interval
Formula Steps: seed
Example Data:
Expected Result: 

Task 36: Confidence Interval For a Sample Function
User Story: Developer wants to calculate the confidence interval for a sample function
Formula Steps: conf, data, seed, higher
Example Data:
Expected Result: 

Task 37: Margin of Error Function
User Story: Developer wants to calculate margin of error of a data set
Formula Steps: seed, data, multiplication 
Example Data:
Expected Result: 

Task 38: How to Find Confidence Interval Function
User Story: Developer wants to calculate confidence interval for a data set
Formula Steps: ---
Example Data:
Expected Result: 

Task 39: Cochran’s Formula Function
User Story: Developer wants to calculate an ideal sample size given a desired level of precision, desired confidence level, and the estimated proportion of the attribute present in the population
Formula Steps: seed, data, range
Example Data:
Expected Result: 

Task 40: Find Sample Size Unknown Pop and StdDev Function
User Story: Developer wants to calculate a sample size given a standard deviation and without being given a population.
Formula Steps: seed, data, percentage, exponentiation
Example Data:
Expected Result: 

Task 41: Find Sample Size Known Pop and StdDev Function
User Story: Developer wants to calculate a sample size given a standard deviation and a population.
Formula Steps: seed, data, exponent
Example Data:
Expected Result: 




[![Build Status](https://travis-ci.org/kaw393939/gettingstartedDockerIS218.svg?branch=master)](https://travis-ci.org/kaw393939/gettingstartedDockerIS218)
# My Calculator Program
This program performs basic arithemtic operations.
