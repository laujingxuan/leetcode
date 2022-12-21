# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.


class Solution:
    def partition(self, s):
        output = []
        self.partitionHelper(s, output, [])
        return output

    def partitionHelper(self, s, output, currentCombi):
        if s == "":
            print(s)
            output.append(currentCombi[:])
            return
        print("before s:" + s)
        for i in range(1, len(s)+ 1):
            temp = s[0:i]
            # print("temp:" + temp)
            if not self.isPalindrome(temp):
                # print("self:" + temp)
                continue
            currentCombi.append(temp)
            print("after s:" + s)
            self.partitionHelper(s[i:], output, currentCombi)
            del currentCombi[-1]
        return


    def isPalindrome(self, s):
        firstIndex = 0
        lastIndex = len(s) - 1
        while lastIndex > firstIndex:
            if s[firstIndex] != s[lastIndex]:
                return False
            lastIndex -= 1
            firstIndex += 1
        return True

if __name__ == "__main__":
    test = Solution()
    print(test.partition("aab"))