class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 0 or numerator == 0:
            return "0"
        
        #without using float division
        res = ""
        if numerator < 0 and denominator > 0 or numerator > 0 and denominator < 0:
            res = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        res += str(numerator//denominator)
        numerator = numerator % denominator
        if numerator == 0:
            return res
        res += "."
        trackMap = {}
        trackMap[numerator] = len(res)
        while numerator > 0:
            numerator *= 10
            res += str(numerator//denominator)
            numerator = numerator % denominator
            if numerator in trackMap:
                index = trackMap[numerator]
                res = res[:index] + "(" + res[index:] + ")"
                break
            trackMap[numerator] = len(res)
        return res
