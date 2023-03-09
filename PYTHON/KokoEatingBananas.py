# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.


class Solution:
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        while right > left:
            mid = (right + left)//2
            if self.checkNumOfHoursNeeded(piles, mid) > h:
                left = mid + 1
                continue
            right = mid
        return right


    def checkNumOfHoursNeeded(self, piles, k):
        count = 0
        for pile in piles:
            count += math.ceil(pile/k)
        return count

    def minEatingSpeedTimeLimitedExceeded(self, piles, h):
        minPiles = 1
        maxPiles = max(piles)
        for i in range(minPiles, maxPiles + 1):
            if h == self.checkNumOfHoursNeeded(piles, i):
                return i
        return -1

    def checkNumOfHoursNeeded(self, piles, k):
        count = 0
        for pile in piles:
            count += math.ceil(pile/k)
        return count