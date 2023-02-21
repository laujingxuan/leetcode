# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
# Return a list of integers representing the size of these parts.

from cgi import parse_multipart


class Solution:

    def partitionLabel(self, s):
        latestAppearance = {}
        for i in range(len(s)):
            latestAppearance[s[i]] = i
        partitions = []
        maxIndex = 0
        prev = -1
        for i in range(len(s)):
            latestIndex = latestAppearance[s[i]]
            maxIndex = max(maxIndex, latestIndex)
            if i == maxIndex:
                partitions.append(maxIndex - prev)
                prev = maxIndex
        return partitions


    def partitionLabelsStupidWay(self, s):
        checkMap = {}
        partitions = []
        for i in range(len(s)):
            if s[i] in checkMap:
                startIndex = checkMap[s[i]]
                partitions.append([startIndex, i])
                continue
            checkMap[s[i]] = i
        partitions.sort(key= lambda x:x[0])
        if len(partitions) == 0:
            return [1] * len(s)
        output = []
        lastNum = partitions[0][1]
        firstNum = partitions[0][0]
        if partitions[0][0] > 0:
            for z in range(0, partitions[0][0]):
                output.append(1)        
        for i in range(1, len(partitions)):
            if partitions[i][0] > lastNum:
                output.append(lastNum-firstNum + 1)
                for z in range(lastNum + 1, partitions[i][0]):
                    output.append(1)
                firstNum = partitions[i][0]
                lastNum = partitions[i][1]
                continue
            lastNum = max(lastNum, partitions[i][1])
        output.append(lastNum-firstNum+1)
        if lastNum + 1 < len(s):
            for z in range(lastNum + 1, len(s)):
                output.append(1)    
        return output




if __name__ == "__main__":
    s= "ababcbacadefegdehijhklij"
    test = Solution()
    # print(test.partitionLabels(s))
    # s1 = "caedbdedda"
    # print(test.partitionLabels(s1))
    s2 = "bbvemgjwruuwalp"
    print(test.partitionLabels(s2))