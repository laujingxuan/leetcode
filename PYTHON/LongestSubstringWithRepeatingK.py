class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        trackMap = {}
        for i in range(len(s)):
            trackMap[s[i]] = trackMap.get(s[i], 0) + 1

        notValidSet = set()
        for key in trackMap:
            if trackMap[key] < k:
                notValidSet.add(key)
        
        maxSubStringLength = 0
        start = 0
        if len(notValidSet) <= 0:
            return len(s)
        for i in range(len(s)):
            if s[i] in notValidSet:
                maxSubStringLength = max(maxSubStringLength, self.longestSubstring(s[start:i], k))
                start = i + 1
        maxSubStringLength = max(maxSubStringLength, self.longestSubstring(s[start:], k))

        return maxSubStringLength

if __name__ == "__main__":
    test = Solution()
    print(test.longestSubstring("bbaaacbd", 3))