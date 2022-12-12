class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        checkMap = {}
        longestLength = 0
        firstIndex = 0
        secondIndex = 0
        while secondIndex < len(s):
            if s[secondIndex] in checkMap:
                firstIndex = max(firstIndex, checkMap[s[secondIndex]] + 1)
            longestLength = max(secondIndex-firstIndex, longestLength)
            checkMap[s[secondIndex]] = secondIndex
            secondIndex += 1
        return longestLength + 1

if __name__ == "__main__":
    test = Solution()
    print(test.lengthOfLongestSubstring("tmmzuxt"))