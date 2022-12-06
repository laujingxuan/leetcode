class Solution:

    #time complexity (O(N)) and space complexity of O(N)
    def longestPalindrome(self, words):
        checkMap = {}
        totalCount = 0
        for i in range(len(words)):
            reversed = words[i][1] + words[i][0]
            if reversed in checkMap:
                totalCount += 4
                checkMap[reversed] -= 1
                if checkMap[reversed] <=0:
                    del checkMap[reversed]
            elif words[i] in checkMap:
                checkMap[words[i]] += 1
            else:
                checkMap[words[i]] = 1
        for key in checkMap:
            if key[0] == key[1]:
                totalCount +=2
                break
        return totalCount

    #time complexity (O(N^2)) and space complexity of O(N)
    def longestPalindromeNonIdeal(self, words):
        longest = 0
        usedSet = set()
        duplicateUsed = False
        for i in range(len(words)):
            if i in usedSet:
                continue
            added = False
            if i < len(words) - 1:
                for j in range(i+1, len(words)):
                    if j in usedSet:
                        continue
                    if words[i] == (words[j][1] + words[j][0]):
                        print(str(i) + ":" + str(j))
                        print(words[i] + ":" + words[j])
                        longest += 4
                        usedSet.add(j)
                        added=True
                        break
            if not added and not duplicateUsed and words[i][0] == words[i][1]:
                longest += 2
                duplicateUsed = True
                print("check")
                continue                    
        return longest


if __name__ == "__main__":
    test = Solution()
    # print(test.longestPalindrome(["cc","cc"]))
    # print(test.longestPalindrome(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]))
    print(test.longestPalindrome(["em","pe","mp","ee","pp","me","ep","em","em","me"]))
    # print(test.longestPalindrome(["ll","lb","bb","bx","xx","lx","xx","lx","ll","xb","bx","lb","bb","lb","bl","bb","bx","xl","lb","xx"]))