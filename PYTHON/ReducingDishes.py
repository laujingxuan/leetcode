# A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

# Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

# Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.

# Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.

class Solution:

    def maxSatisfaction(self, satisfaction):
        satisfaction.sort()
        ans = 0
        currentTotal = 0
        for i in range(len(satisfaction) - 1, -1, -1):
            currentTotal += satisfaction[i]
            if currentTotal <= 0:
                break
            ans += currentTotal

        return ans

    def maxSatisfactionOkButCanBeImproved(self, satisfaction):
        satisfaction.sort()
        maxSatisfaction = satisfaction[-1]
        # if all -ve value, then just return 0
        if maxSatisfaction <= 0:
            return 0

        # find the totalPositive value
        positiveSum = 0
        for i in range(len(satisfaction)):
            if satisfaction[i] > 0:
                positiveSum += satisfaction[i]

        # find the index where the sum of negative values start to > positive value
        startIndex = len(satisfaction) - 2
        negativeSum = 0
        for i in range(len(satisfaction) - 1, -1, -1):
            if satisfaction[i] < 0:
                negativeSum += satisfaction[i]
                if -negativeSum >= positiveSum:
                    break
            startIndex = i

        # find the total from the index
        ans = 0
        for i in range(startIndex, len(satisfaction)):
            ans += satisfaction[i] * (i - startIndex + 1)

        return ans

    def maxSatisfactionTimeLimitExceeded(self, satisfaction):
        satisfaction.sort()
        self.ans = 0
        self.helper(satisfaction, 0, 0, 1)
        return self.ans

    def helper(self, satisfaction, index, currentSum, currentMultiplier):
        if index >= len(satisfaction):
            self.ans = max(currentSum, self.ans)
            return

        #take
        self.helper(satisfaction, index + 1, currentSum + satisfaction[index] * currentMultiplier, currentMultiplier + 1)
        
        if satisfaction[index] < 0:
            #dont take
            self.helper(satisfaction, index + 1, currentSum, currentMultiplier)

        return