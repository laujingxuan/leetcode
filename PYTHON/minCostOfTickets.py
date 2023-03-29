# You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

# Train tickets are sold in three different ways:

# a 1-day pass is sold for costs[0] dollars,
# a 7-day pass is sold for costs[1] dollars, and
# a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.

# For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
# Return the minimum number of dollars you need to travel every day in the given list of days.

class Solution:
    def mincostTicketsTimeLimitExceeded(self, days, costs):
        costsMap = {costs[0]:1, costs[1]:7, costs[2]:30}
        return self.backTrackHelper(days, costsMap, 0, 0)

    def backTrackHelper(self, days, costsMap, daysIndex, maxDay):
        if daysIndex >= len(days):
            return 0
        if maxDay >= days[daysIndex]:
            return self.backTrackHelper(days, costsMap, daysIndex + 1, maxDay)

        today = days[daysIndex]
        minCost = math.inf
        for cost in costsMap:
            minCost = min(minCost, self.backTrackHelper(days, costsMap, daysIndex + 1, today + costsMap[cost] - 1) + cost)

        return minCost