# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Input: s = "a", t = "a"
# Output: "a"
# Input: s = "a", t = "aa"
# Output: ""
class Solution:
    def minWindow(self, s, t):
        if len(s) < len(t):
            return ""
        shortestSubstring = s + "a"
        firstIndex = 0
        secondIndex = 0
        trackCount = len(t)
        checkMap = {}
        for char in t:
            if char in checkMap:
                checkMap[char] += 1
            else:
                checkMap[char] = 1
        print(trackCount)
        while secondIndex < len(s):
            print(checkMap)
            if s[secondIndex] in checkMap:
                checkMap[s[secondIndex]] -= 1
                if checkMap[s[secondIndex]] >= 0:
                    trackCount -= 1
                print(trackCount)
            while trackCount == 0:
                if secondIndex - firstIndex < len(shortestSubstring):
                    shortestSubstring = s[firstIndex: secondIndex + 1]
                if s[firstIndex] in checkMap:
                    checkMap[s[firstIndex]] += 1
                    if checkMap[s[firstIndex]] > 0:
                        trackCount += 1
                firstIndex += 1
            secondIndex += 1
        if len(shortestSubstring) > len(s):
            return ""
        return shortestSubstring


if __name__ == "__main__":
    test = Solution()
    print(test.minWindow("ADOBECODEBANC", "ABC"))