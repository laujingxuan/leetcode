class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        for i in range(1, len(strs)):
            newCommon = ""
            for j in range(len(common)):
                if j >= len(strs[i]) or common[j] != strs[i][j]:
                    break
                newCommon += common[j]
            common = newCommon
            if newCommon == "":
                break
        return common

    # Different question
    def longestCommonStrings(self, strs):
        common = strs[0]
        for i in range(1, len(strs)):
            memo = [["A" for i in range(len(common))] for j in range(len(strs[i]))]
            common = self.longestHelper(strs[i], common, memo, 0, 0, "")
        return common
    
    def longestHelper(self, str1, str2, memo, index1, index2, currentCombi):
        if index1 >= len(str1) or index2 >= len(str2):
            return currentCombi
        if memo[index1][index2] != "A":
            return memo[index1][index2]
        if str1[index1] == str2[index2]:
            memo[index1][index2] =  self.longestHelper(str1,str2,memo,index1 + 1, index2 + 1, currentCombi + str1[index1])
            return memo[index1][index2]
        firstPossibility = self.longestHelper(str1, str2, memo, index1 + 1, index2, "")
        secondPossibility = self.longestHelper(str1, str2, memo, index1, index2 + 1, "")
        if len(currentCombi) >= len(firstPossibility) and len(currentCombi) >= len(secondPossibility):
            memo[index1][index2] = currentCombi
        elif len(firstPossibility) > len(currentCombi) and len(firstPossibility) > len(secondPossibility):
            memo[index1][index2] = firstPossibility
        else:
            memo[index1][index2] = secondPossibility
        
        return memo[index1][index2]

if __name__ == "__main__":
    test = Solution()
    # print(test.longestCommonPrefix(["flower","flow","flight"]))
    print(test.longestCommonPrefix(["ca","a"]))