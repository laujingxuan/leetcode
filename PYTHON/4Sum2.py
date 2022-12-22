# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        firstMap = {}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                current = nums1[i] + nums2[j]
                if current in firstMap:
                    firstMap[current] += 1
                else:
                    firstMap[current] = 1
        totalCount = 0
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                current = - nums3[i] - nums4[j]
                if current in firstMap:
                    totalCount += firstMap[current]
        return totalCount

if __name__ == "__main__":
    test = Solution()
    print(test.fourSumCount([1,2], [-2,-1], [-1,2], [0,2]))