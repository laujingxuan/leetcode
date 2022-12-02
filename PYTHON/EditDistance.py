class Solution:
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character
 
    #bottom up approach
    def minDistance(self, word1: str, word2: str) -> int:
        tracking = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0 or j == 0:
                    tracking[i][j] = i + j
                elif word1[i-1] == word2[j-1]:
                    tracking[i][j] = tracking[i-1][j-1]
                else:
                    tracking[i][j] = 1 + min(tracking[i-1][j-1], tracking[i-1][j], tracking[i][j-1])
        return tracking[len(word1)][len(word2)]

    #dp approach
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[0 for i in range(len(word2))] for j in range(len(word1))]
        return self.minDistanceHelper(word1, word2, 0, 0, memo)

    def minDistanceHelper(self, word1, word2, index1, index2, memo):
        if index1 == len(word1) and index2 == len(word2):
            return 0
        if index1 == len(word1):
            return len(word2) - index2
        if index2 == len(word2):
            return len(word1) - index1
    
        if memo[index1][index2] != 0:
            return memo[index1][index2]

        if word1[index1] == word2[index2]:
            memo[index1][index2] = self.minDistanceHelper(word1, word2, index1 + 1, index2 + 1, memo)
        else:
            addCount = 1 + self.minDistanceHelper(word1, word2, index1 + 1, index2, memo)
            deleteCount = 1 + self.minDistanceHelper(word1, word2, index1, index2 + 1, memo)
            swapCount = 1 + self.minDistanceHelper(word1, word2, index1 + 1, index2 + 1, memo)
            memo[index1][index2] = min(addCount, deleteCount, swapCount)
        return memo[index1][index2]