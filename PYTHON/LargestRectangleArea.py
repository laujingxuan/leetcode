class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0)
        stack = [-1]
        maxArea = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                #height of rectangle will be height * distance between two boundaries of shorter height
                width = i - 1 - stack[-1]
                maxArea = max(maxArea, width * height)
            stack.append(i)

        return maxArea