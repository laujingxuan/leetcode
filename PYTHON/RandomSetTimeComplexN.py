import random


class RandomizedSet:

    def __init__(self):
        self.mydict = {}
        self.myList = []

    def insert(self, val: int) -> bool:
        if val in self.mydict:
            return False
        self.mydict[val] = len(self.myList)
        self.myList.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.mydict:
            index = self.mydict[val]
            self.mydict[self.myList[-1]] = index
            self.myList[index] = self.myList[-1]
            del self.myList[-1]
            del self.mydict[val]
            return True
        return False

    def getRandom(self) -> int:
        randomIndex = random.randrange(len(self.myList))
        return self.myList[randomIndex]