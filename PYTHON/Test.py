import math
import random


class Solution:
    # def partition(self, input, low, high):
    #     randIndex = random.randrange(low, high+1)
    #     input[randIndex], input[high] = input[high], input[randIndex]
    #     target = input[high]
    #     index = low
    #     for i in range(low, high):
    #         if input[i] <= target:
    #             input[index], input[i] = input[i], input[index]
    #             index += 1
    #     input[high], input[index] = input[index], input[high]
    #     return index

    # def randomizedQuickSort(self, input, low, high):
    #     if low < high:
    #         correctIndex = self.partition(input, low, high)
    #         self.randomizedQuickSort(input, low, correctIndex - 1)
    #         self.randomizedQuickSort(input, correctIndex + 1, high)
    #     return input
            
    # def heapify(self, array, currentIndex, lastIndex):
    #     maxIndex = currentIndex
    #     if 2 * currentIndex + 1 <= lastIndex and array[2*currentIndex + 1] > array[maxIndex]:
    #         maxIndex = 2 * currentIndex + 1
    #     if 2 * currentIndex + 2 <= lastIndex and array[2*currentIndex + 2] > array[maxIndex]:
    #         maxIndex = 2 * currentIndex + 2
    #     if maxIndex != currentIndex:
    #         array[currentIndex], array[maxIndex] = array[maxIndex], array[currentIndex]
    #         self.heapify(array, maxIndex, lastIndex)
    #     return

    # def heapSort(self, input):
    #     for i in range(len(input) - 1, -1, -1):
    #         self.heapify(input, i, len(input) - 1)
    #     index = len(input) - 1
    #     while index > 0:
    #         input[index], input[0] = input[0], input[index]
    #         index -= 1
    #         self.heapify(input, 0, index)
    #     return input

    def heapify(self, nums, index, end):
        maxIndex = index
        leftChild = 2*index + 1
        rightChild = 2*index + 2
        if leftChild <= end and nums[leftChild] > nums[maxIndex]:
            maxIndex = leftChild
        if rightChild <= end and nums[rightChild] > nums[maxIndex]:
            maxIndex = rightChild
        if maxIndex != index:
            nums[maxIndex], nums[index] = nums[index], nums[maxIndex]
            self.heapify(nums, maxIndex, end)
        return

    def heapSort(self, nums):
        for i in range((len(nums) - 2)//2, -1, -1):
            self.heapify(nums, i, len(nums) - 1)
        
        for i in range(len(nums)-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, 0, i - 1)
        return nums

if __name__ == "__main__":
    # test = Solution()
    # input = [319776,611683,835240,602298,430007,574,142444,858606,734364,896074]
    # print(1766699 + 602298)
    testOne = None
    print(3*"a")
    # print(test.maxSubarraySumCircular(input))
    # test.quickSort(input, 0, len(input) - 1)
    # test.heapSort(input)
    # print(input)
    # print(test.mergeSort(input))
    # print(14//3)
    # print(test.binarySearch(input, 3))
    # print(test.mergeSort([8,5,7,9,10,1,3,2]))
    # test = [[0] * 3 for i in range(3)]
    # piles = [5,3,4,5]
    # memo = [[[-1 for i in range(len(piles))] for j in range(len(piles))]for z in range(2)]
    # print(test)
    # print(memo)
    # print(type(math.inf))