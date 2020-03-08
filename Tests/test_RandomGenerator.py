import unittest
from RandomData.RandomData import getRandomNums
from RandomGenerator.RandomList import RandomList
from RandomGenerator.randomNoSeed import RandomNoSeed
from RandomGenerator.RandomWithSeed import RandomWithSeed
from RandomGenerator.SelectWithoutSeed import SelectWithoutSeed
from RandomGenerator.SelectItemList import SelectItemList


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.testData = getRandomNums(1, 1, 100, 20)

    def test_RandomListInt(self):
        result = RandomList.listInt(0, 10, 5, 4)
        self.assertEqual(result, [7, 5, 1, 8, 7])

    def test_RandomListDec(self):
        result = RandomList.listDec(0, 10, 5, 4)
        self.assertEqual(result, [9.670298390136766, 5.4723224917572235,
                                  9.726843599648843, 7.148159936743647,
                                  6.977288245972709])
    def test_RandomNoSeed_Int(self):
        result = RandomNoSeed.randomInt(0, 10)
        self.assertEqual(isinstance(result, int), True)

    def test_RandomNoSeed_Dec(self):
        result = RandomNoSeed.randomDec(0, 10)
        self.assertEqual(isinstance(result, float), True)

    def test_RandomSeed_Int(self):
        result = RandomWithSeed.randomInt(4, 0, 10)
        result2 = RandomWithSeed.randomInt(4, 0, 10)
        self.assertEqual(result, result2)

    def test_RandomSeed_Dec(self):
        result = RandomWithSeed.randomDec(4, 0, 10)
        result2 = RandomWithSeed.randomDec(4, 0, 10)
        self.assertEqual(result, result2)

    def test_PickRandomNumber(self):
        lst = RandomList.listInt(0, 10, 5, 4)
        result = SelectItemList.pickItem(lst)
        self.assertEqual(len(result), 1)




if __name__ == '__main__':
    unittest.main()