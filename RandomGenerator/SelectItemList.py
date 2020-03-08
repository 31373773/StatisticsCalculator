from numpy.random import randint

class SelectItemList():
    @staticmethod
    def pickItem(lst, rnge):
        lst2 =[]
        length = len(lst)
        for each in range(rnge):
            position = randint(0, length-1)
            lst2.append(lst[position])

        return lst2