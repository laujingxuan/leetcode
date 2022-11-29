#A message containing letters from A-Z can be encoded into numbers using the following mapping:
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
def numDecodings(s):
    checkMap = {"A":1, "B":2, "C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
    
def numDecodingsHelper(s, memo, index, checkMap):
    if index >= len(s):
        return 1
    


if __name__ == "__main__":
    print(numDecodings("226"))