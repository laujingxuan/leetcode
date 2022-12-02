from collections import Counter


class Solution:
    def closeStringsPythonBestAnswer(self, word1: str, word2: str) -> bool:
        return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())

    def closeStrings(self, word1: str, word2: str) -> bool:
        word1Track = {}
        for i in range(len(word1)):
            if word1[i] in word1Track:
                word1Track[word1[i]] = word1Track[word1[i]] + 1
            else:
                word1Track[word1[i]] = 1

        word2Track = {}
        for i in range(len(word2)):
            if word2[i] not in word1Track:
                return False
            elif word2[i] in word2Track:
                word2Track[word2[i]] = word2Track[word2[i]] + 1
            else:
                word2Track[word2[i]] = 1

        word1Counts = list(word1Track.values())
        word1Counts.sort()
        word2Counts = list(word2Track.values())
        word2Counts.sort()
        return word1Counts == word2Counts
        # noOfOccWord1 = {}
        # for char in word1Track:
        #     count = word1Track[char]
        #     if count in noOfOccWord1:
        #         noOfOccWord1[count] = noOfOccWord1[count] + 1
        #     else:
        #         noOfOccWord1[count] = 1
        
        # noOfOccWord2 = {}
        # for char in word2Track:
        #     count = word2Track[char]
        #     if count in noOfOccWord2:
        #         noOfOccWord2[count] = noOfOccWord2[count] + 1
        #     else:
        #         noOfOccWord2[count] = 1

        # for charFirstNoOcc in noOfOccWord1:
        #     if charFirstNoOcc in noOfOccWord2 and noOfOccWord1[charFirstNoOcc] == noOfOccWord2[charFirstNoOcc]:
        #         del noOfOccWord2[charFirstNoOcc]
        #     else:
        #         return False
        
        # if len(noOfOccWord2) != 0:
        #     return False
        # return True
                 
        
