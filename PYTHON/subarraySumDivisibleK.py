# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
# A subarray is a contiguous part of an array.
# -104 <= nums[i] <= 104

class Solution:
    #time complexity of O(N^2)
    def subarraysDivByKBruteForce(self, nums, k):
        count = 0
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                print(total)
                if total % k == 0:
                    count += 1
        return count

    def subarraysDivByKBetter(self, nums, k):    
        checkMap = {0:1}
        total = 0
        totalSubArray = 0
        for num in nums:
            total += num
            remainder = total%k
            if remainder in checkMap:
                totalSubArray += checkMap[remainder]
            count = checkMap.get(remainder, 0)
            checkMap[remainder] = count + 1
        return totalSubArray

    #two for loop where above only one
    def subarraysDivByKSlightlyLessIdeal(self, nums, k):
        prefixSumArrayRemainder = [0] * len(nums)
        prefixSum = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            prefixSumArrayRemainder[i] = prefixSum % k
        
        checkMap = {}
        checkMap[0] = 1
        count = 0
        for i in range(len(prefixSumArrayRemainder)):
            if prefixSumArrayRemainder[i] in checkMap:
                count += checkMap[prefixSumArrayRemainder[i]]
                checkMap[prefixSumArrayRemainder[i]] += 1
            else:
                checkMap[prefixSumArrayRemainder[i]] = 1
        return count
        

if __name__ == "__main__":
    test = Solution()
    print(test.subarraysDivByK([4,5,0,-2,-3,1], 5))
    # print(test.subarraysDivByK([5], 9))