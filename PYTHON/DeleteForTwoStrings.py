# Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
# In one step, you can delete exactly one character in either string.

def minDistance(word1, word2):
    memo = [[-1 for i in range(len(word2))] for j in range(len(word1))]
    return minDistanceHelper(word1, word2, 0, 0, memo)

def minDistanceHelper(word1, word2, index1, index2, memo):
    if index1 == len(word1):
        return len(word2) - index2
    if index2 == len(word2):
        return len(word1) - index1
    if memo[index1][index2] != -1:
        return memo[index1][index2]
    if word1[index1] == word2[index2]:
        memo[index1][index2] = minDistanceHelper(word1, word2, index1 + 1, index2 + 1, memo)
    else:
        memo[index1][index2] = 1 + min(minDistanceHelper(word1, word2, index1 + 1, index2, memo), minDistanceHelper(word1, word2, index1, index2 + 1, memo))
    return memo[index1][index2]

def minDistanceBottomUp(word1, word2):
    memo = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
    for i in range(len(word1) + 1):
        for j in range(len(word2) + 1):
            # In the start, if i == 0 or j == 0, one string is of length 0 and we have no choice but to delete all characters from the other string to equalize them both.
            if i == 0 or j == 0:
                memo[i][j] = i +j
            elif word1[i - 1] == word2[j-1]:
                memo[i][j] = memo[i-1][j-1]
            else:
                memo[i][j] = 1 + min(memo[i-1][j], memo[i][j-1])
    return memo[len(word1)][len(word2)]


if __name__ == "__main__":
    print(minDistance("sea", "eat"))
    print(minDistanceBottomUp("sea", "eat"))