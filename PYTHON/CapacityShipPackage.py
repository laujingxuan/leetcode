import math

# A conveyor belt has packages that must be shipped from one port to another within days days.
# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
class Solution:
    def shipWithinDays(self, weights, days):
        minPossibleCapacity = max(weights)
        maxPossibleCapacity = sum(weights)
        while maxPossibleCapacity > minPossibleCapacity:
            mid = (maxPossibleCapacity + minPossibleCapacity)//2
            curr = 0
            need = 1
            for w in weights:
                curr += w
                if curr > mid:
                    need += 1
                    curr = w
            if need > days:
                minPossibleCapacity = mid + 1
            else:
                maxPossibleCapacity = mid
        return minPossibleCapacity


    def shipWithinDaysTimeLimitExceeded(self, weights, days: int) -> int:
        return self.helper(weights, days, 0, 0)

    def helper(self, weights, days, index, minCapacity):
        if index == len(weights) and days == 0:
            return minCapacity
        if days == 0 or index >= len(weights):
            return -1

        outputMinCapacity = math.inf
        for i in range(index, len(weights)):
            newMinCapacity = max(minCapacity, sum(weights[index:i+1]))
            found = self.helper(weights, days - 1, i + 1, newMinCapacity)
            if found != -1:
                outputMinCapacity = min(outputMinCapacity, found)
        return outputMinCapacity