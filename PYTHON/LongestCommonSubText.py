# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.
def longestCommonSubsequence(text1, text2):
    memo = [[-1 for i in range(len(text2))] for j in range(len(text1))]
    return longestHelper(text1, text2, 0,0,memo)

def longestHelper(text1, text2, oneIndex, twoIndex, memo):
    if oneIndex >= len(text1) or twoIndex >= len(text2):
        return 0
    if memo[oneIndex][twoIndex] == -1:
        if text1[oneIndex] == text2[twoIndex]:
            memo[oneIndex][twoIndex] = 1 + longestHelper(text1, text2, oneIndex + 1, twoIndex + 1, memo)
        else:
            memo[oneIndex][twoIndex] = max(longestHelper(text1, text2, oneIndex + 1, twoIndex, memo), longestHelper(text1, text2, oneIndex, twoIndex + 1, memo))
    return memo[oneIndex][twoIndex]

def longestCommonSubsequenceBottomUp(text1, text2):
    memo = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
    for i in range(1,len(text1)+1):
        for j in range(1,len(text2)+1):
            if text1[i-1] == text2[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])
    return memo[len(text1)][len(text2)]

if __name__ == "__main__":
    # print(longestCommonSubsequence("abcde", "ace"))
    # print(longestCommonSubsequence("abc", "abc"))
    # print(longestCommonSubsequence("abc", "def"))
    # print(longestCommonSubsequence("abcba", "abcbcba"))
    print(longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd"))
    print(longestCommonSubsequenceBottomUp("pmjghexybyrgzczy", "hafcdqbgncrcbihkd"))

