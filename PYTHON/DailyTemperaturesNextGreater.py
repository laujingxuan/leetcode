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