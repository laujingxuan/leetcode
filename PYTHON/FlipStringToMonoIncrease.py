import math


class Solution:
    #multiple pass
    def minFlipsMonoIncrSlightlyNotIdeal(self, s: str) -> int:
        minFlipsArray = [0] * len(s)
        oneCount = 0
        for i in range(1, len(s)):
            if s[i - 1] == "1":
                oneCount += 1
            minFlipsArray[i] += oneCount
        zeroCount = 0
        for i in range(len(s)-2, -1, -1):
            if s[i + 1] == "0":
                zeroCount += 1
            minFlipsArray[i] += zeroCount
        minFlip = math.inf
        for i in range(len(minFlipsArray)):
            minFlip = min(minFlipsArray[i], minFlip)
        return minFlip

    #one pass solution
    def minFlipsMonoIncr(self, s: str) -> int:
        oneCount = 0
        flippingCount = 0
        for i in range(len(s)):
            if s[i] == "0":
                if oneCount == 0:
                    continue
                else:
                    flippingCount += 1
            else:
                oneCount += 1
            if flippingCount > oneCount:
                flippingCount = oneCount
        return flippingCount