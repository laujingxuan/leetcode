import heapq
import math

class Solution:

    def minimumDeviation(self, nums):
        #find the largest odd number
        heap = []
        maxNumber = 0
        minDifference = math.inf
        for num in nums:
            oriValue = num
            while num%2==0:
                num = num//2
            heapq.heappush(heap, [num, oriValue])
            maxNumber = max(maxNumber, num)
        while len(heap) == len(nums):
            combi = heapq.heappop(heap)
            minDifference = min(minDifference, maxNumber - combi[0])
            if combi[0] % 2 == 1 or combi[0] < combi[1]:
                combi[0] = combi[0] * 2
                maxNumber = max(maxNumber, combi[0])
                heapq.heappush(heap, combi)
        return minDifference


    #Non ideal
    def minimumDeviationTimeLimitExceeded(self, nums):
        self.ans = math.inf
        self.backtrack(nums, 0, [])
        return self.ans

    def backtrack(self, nums, index, combi):
        if index >= len(nums):
            maxValue = max(combi)
            minValue = min(combi)
            self.ans = min(self.ans, maxValue-minValue)
            return
        targetIndexValue = nums[index]
        combi.append(targetIndexValue)
        self.backtrack(nums, index+1, combi)
        del combi[-1]

        if targetIndexValue % 2 == 1:
            combi.append(targetIndexValue * 2)
            self.backtrack(nums, index+1, combi)
            del combi[-1]
        
        while targetIndexValue % 2 == 0:
            targetIndexValue = targetIndexValue//2
            combi.append(targetIndexValue)
            self.backtrack(nums, index+1, combi)
            del combi[-1]        
        return