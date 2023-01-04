class Solution:
    #O(N) space complexity and O(N) time complexity
    def minimumRoundsMathSolution(self, tasks):
        trackMap = {}
        for i in range(len(tasks)):
            if tasks[i] in trackMap:
                trackMap[tasks[i]] += 1
                continue
            trackMap[tasks[i]] = 1
        
        totalRounds = 0
        for key in trackMap:
            if trackMap[key] == 1:
                return -1
            remainder = trackMap[key]%3
            countThree = trackMap[key]//3
            if remainder == 0:
                totalRounds += countThree
            else:
                totalRounds += countThree + 1
        return totalRounds

    #O(N) space complexity for map used and length of memo of maximum count
    #O(N) time complexity as memo is used and hence maximum recursion is maximum count
    def minimumRoundsNonIdeal(self, tasks):
        trackMap = {}
        maxCountForDifficulty = 0
        for i in range(len(tasks)):
            if tasks[i] in trackMap:
                trackMap[tasks[i]] += 1
            else:
                trackMap[tasks[i]] = 1
            maxCountForDifficulty = max(maxCountForDifficulty, trackMap[tasks[i]])

        totalRoundsNeeded = 0
        memo = [-1 for i in range(maxCountForDifficulty + 1)]
        for key in trackMap:
            if trackMap[key] > 1:
                roundNeeded = self.checkRoundsNeeded(trackMap[key], memo)
                if roundNeeded > 0:
                    totalRoundsNeeded += roundNeeded
                    continue
            return -1
        print(memo)
        return totalRoundsNeeded

    def checkRoundsNeeded(self, value, memo):
        if value < 0:
            return -1
        if value == 0:
            return 0
        if memo[value] != -1:
            return memo[value]
        first = self.checkRoundsNeeded(value-3, memo)
        second = self.checkRoundsNeeded(value-2, memo)
        if first > -1 and second > -1:
            memo[value] = min(first, second) + 1
        elif first > -1:
            memo[value] = first + 1
        elif second > -1:
            memo[value] = second + 1
        return memo[value]

if __name__ == "__main__":
    test = Solution()
    print(test.minimumRoundsNonIdeal([2,2,3,3,2,4,4,4,4,4]))
    print(test.minimumRoundsNonIdeal([5,5,5,5]))



