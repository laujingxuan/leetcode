# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        self.flatList = self.checkType(nestedList)
        self.index = 0

    def checkType(self, value):
        output = []
        if type(value) is list:
            for i in range(len(value)):
                foundValues = self.checkType(value[i])
                output = output + foundValues
            return output
        output.append(value)
        return output
    
    def next(self) -> int:
        toReturn = self.flatList[self.index]
        self.index += 1
        return toReturn
    
    def hasNext(self) -> bool:
        if self.index < len(self.flatList):
            return True
        return False 

if __name__ == "__main__":
    i, v = NestedIterator([[1,1],2,[1,1]]), []
    while i.hasNext(): v.append(i.next())
    print(v)


#With NestedInteger value type being passed
# class NestedIterator:
#     def __init__(self, nestedList: [NestedInteger]):
#         self.flatList = []
#         for i in range(len(nestedList)):
#             self.flatList += self.checkType(nestedList[i])
#         self.index = 0
#         # print(self.flatList)

#     def checkType(self, value):
#         output = []
#         if not value.isInteger():
#             for i in range(len(value.getList())):
#                 foundValues = self.checkType(value.getList()[i])
#                 output = output + foundValues
#             return output
#         output.append(value.getInteger())
#         return output
    
#     def next(self) -> int:
#         toReturn = self.flatList[self.index]
#         self.index += 1
#         return toReturn
    
#     def hasNext(self) -> bool:
#         if self.index < len(self.flatList):
#             return True
#         return False 