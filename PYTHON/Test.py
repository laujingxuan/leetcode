class Solution:
    def permute(self, nums):
        output = []
        self.permuteHelper(nums, output, [])
        return output

    def permuteHelper(self, nums, output, currentCombi):
        if len(nums) == 0 :
            output.append(currentCombi[:])
            return
        
        for i in range(len(nums)):
            currentCombi.append(nums[i])

            self.permuteHelper(nums[:i] + nums[i+1:], output, currentCombi)
            currentCombi.pop()
        return

if __name__ == "__main__":
    # test = Solution()
    # print(test.permute([1,2,3]))
    print(3<<2)