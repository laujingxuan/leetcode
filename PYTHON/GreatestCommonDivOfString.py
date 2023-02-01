# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

class Solution:

    def gcdMoreMathSolution(self, str1, str2):
        if str1+str2 != str2+str1:
            return ""
        gcdLength = self.gcd(len(str1), len(str2))
        return str1[:gcdLength]
    
    def gcd(self, long, short):
        if short == 0:
            return long
        return self.gcd(short, long%short)

    #time complexity of O(N^2)
    def gcdOfStringsBetterRecursion(self, str1, str2):
        if len(str1) == 0:
            return str2
        if len(str2) == 0:
            return str1
        
        #make str1 to be always greater length
        if len(str2) > len(str1):
            return self.gcdOfStringsBetterRecursion(str2, str1)
        if str1[:len(str2)] == str2:
            return self.gcdOfStringsBetterRecursion(str1[len(str2):], str2)
        return ""

    #self try
    def gcdOfStringsNotIdeal(self, str1: str, str2: str) -> str:
        shortString = str1
        longString = str2
        if len(shortString) > len(longString):
            shortString = str2
            longString = str1
        trackMap = {}
        return self.commonDivisorHelper(longString, shortString, shortString, trackMap)

    def commonDivisorHelper(self, longString, shortString, divisor, trackMap):
        if len(divisor)==0:
            return ""
        if divisor in trackMap:
            if trackMap[divisor]:
                return divisor
            return ""
        isShortDivisible = self.checkIfDivisible(shortString, divisor)
        isLongDivisible = self.checkIfDivisible(longString, divisor)
        trackMap[divisor] = isLongDivisible and isShortDivisible
        if trackMap[divisor]:
            return divisor
        frontCommon = self.commonDivisorHelper(longString, shortString, divisor[:len(shortString)-1], trackMap)
        backCommon = self.commonDivisorHelper(longString, shortString, divisor[1:], trackMap)
        if len(frontCommon) > len(backCommon):
            return frontCommon
        return backCommon

    def checkIfDivisible(self, target, divisor):
        if len(target)%len(divisor) != 0:
            return False
        start = 0
        while start < len(target):
            if target[start:start+len(divisor)] != divisor:
                return False
            start += len(divisor)
        return True