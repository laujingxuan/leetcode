#A message containing letters from A-Z can be encoded into numbers using the following mapping:
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
def numDecodings(s):
    checkMap = {"1":"A", "2":"B", "3":"C","4":"D","5":"E","6":"F","7":"G","8":"H","9":"I","10":"J","11":"K","12":"L","13":"M","14":"N","15":"O","16":"P","17":"Q","18":"R","19":"S","20":"T","21":"U","22":"V","23":"W","24":"X","25":"Y","26":"Z"}
    memo = [-1]*len(s)
    output = numDecodingsHelper(s, memo, 0, checkMap)
    return output
    
def numDecodingsHelper(s, memo, index, checkMap):
    if index >= len(s):
        return 1
    if memo[index] != -1:
        return memo[index]
    if s[index] not in checkMap:
        return 0
    twoDNumberOfWays = 0
    oneDNumberOfWays = numDecodingsHelper(s, memo, index + 1, checkMap)
    if index + 1 < len(s) and int(s[index:index+2]) < 27:
        twoDNumberOfWays = numDecodingsHelper(s, memo, index + 2, checkMap)
    memo[index]=oneDNumberOfWays + twoDNumberOfWays
    return memo[index]


if __name__ == "__main__":
    print(numDecodings("226"))
    print(numDecodings("12"))
    print(numDecodings("10"))
    print(numDecodings("2101"))