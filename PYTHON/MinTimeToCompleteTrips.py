class Solution:
    def minimumTime(self, time, totalTrips):
        maxPossibleTimeNeeded = min(time) * totalTrips
        #binary search
        left = 0
        right = maxPossibleTimeNeeded
        while right > left:
            mid = (right + left)//2
            tripsMade = self.calTripsMade(time, mid)
            if tripsMade < totalTrips:
                left = mid + 1
            else:
                right = mid
        return left

    def calTripsMade(self, time, timeSpent):
        totalTrips = 0
        for i in range(len(time)):
            totalTrips += timeSpent//time[i]
        return totalTrips

    def minimumTimeTimeLimitExceeded(self, time, totalTrips):
        # time.sort()
        timeSpent = 0
        dupTime = time[:]
        while totalTrips > 0:
            timeSpent += 1
            for i in range(len(dupTime)):
                dupTime[i] -= 1
                if dupTime[i] == 0:
                    totalTrips -= 1
                    dupTime[i] = time[i]
        return timeSpent