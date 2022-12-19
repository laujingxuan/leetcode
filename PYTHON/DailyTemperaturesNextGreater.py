class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        output = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                topIndex = stack.pop()
                output[topIndex] = i - topIndex
            stack.append(i)
        return output

    def dailyTemperaturesBruteForce(self, temperatures):
        output = [0] * len(temperatures)
        for i in range(len(temperatures) - 1):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    output[i] = j - i
                    break
        return output

    def nextGreaterElement(self, nums1, nums2):
        stack = []
        stack.append(nums2[0])
        recordTrack = {}
        for i in range(1, len(nums2)):
            while len(stack) != 0 and stack[-1] < nums2[i]:
                current = stack.pop()
                recordTrack[current] = nums2[i]
            stack.append(nums2[i])
        output = []
        for i in range(len(nums1)):
            if nums1[i] in recordTrack:
                output.append(recordTrack[nums1[i]])
            else:
                output.append(-1)
        return output

    def nextGreaterElements(self, nums):
        if len(nums) == 1:
            return [-1]
        stack = []
        stack.append(0)
        output = [-1] * len(nums)
        for i in range(len(nums) * 2):
            while len(stack) != 0 and nums[stack[-1]] < nums[i%len(nums)]:
                current = stack.pop()
                output[current] = nums[i%len(nums)]
            if output[i%len(nums)] == -1:
                stack.append(i%len(nums))
        return output

# Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.
# Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.
    def nextGreaterElementIII(self, n: int) -> int:
        digitsStr = list(str(n))
        i = len(digitsStr) - 1
        while i > 0:
            if digitsStr[i] > digitsStr[i - 1]:
                hasGreater = True
                break
            i -= 1
        
        if i == 0:
            return -1
        
        toChangeNumber = digitsStr[i - 1]
        smallestIndex = i
        for j in range(i, len(digitsStr)):
            if digitsStr[j] > toChangeNumber and digitsStr[j] <= digitsStr[smallestIndex]:
                smallestIndex = j
        digitsStr[i-1], digitsStr[smallestIndex] = digitsStr[smallestIndex], digitsStr[i - 1]
        output = digitsStr[:i] + digitsStr[i:][::-1]
        intOutput = int(''.join(output))
        if intOutput < 1<<31:
            return intOutput
        else:
            return -1