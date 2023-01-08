class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            front = i + 1
            end = len(nums)-1
            while end > front:
                if nums[i] + nums[front] + nums[end] == 0:
                    output.append([nums[i], nums[front], nums[end]])
                    front += 1
                    while front < len(nums) and nums[front] == nums[front-1]:
                        front+=1
                elif nums[i] + nums[front] + nums[end] > 0:
                    end -= 1
                else: 
                    front += 1
        return output