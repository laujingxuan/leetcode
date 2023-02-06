class Solution:
    #using idea of bucket sort
    def topKFrequent(self, nums, k):
        countMap = {}
        for num in nums:
            count = countMap.get(num, 0)
            countMap[num] = count + 1
        
        bucket = [[] for i in range(len(nums) + 1)]
        for num in countMap:
            array = bucket[countMap[num]]
            array.append(num)
        output = []
        for i in range(len(bucket)-1, -1, -1):
            output += bucket[i]
            if len(output) >= k:
                return output[:k]
        return output

if __name__ == "__main__":
    test = Solution()
    input = [3,0,1,0]
    print(test.topKFrequent(input, 1))
