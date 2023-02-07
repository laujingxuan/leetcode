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

    def heapSort(self, nums):
        #heapify all the parent node starting from bottom
        for i in range((len(nums)-2)//2, -1, -1):
            self.heapify(nums, i, len(nums)-1)

        #convert the list to ascending order
        for i in range(len(nums)-1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, 0, i - 1)
        return

    def heapify(self, nums, index, lastIndex):
        leftChildIndex = 2*index + 1
        rightChildIndex = 2*index + 2
        maxIndex = index
        if leftChildIndex <= lastIndex and nums[maxIndex] < nums[leftChildIndex]:
            maxIndex = leftChildIndex
        if rightChildIndex <= lastIndex and nums[maxIndex] < nums[rightChildIndex]:
            maxIndex = rightChildIndex
        if maxIndex != index:
            nums[index], nums[maxIndex] = nums[maxIndex], nums[index]
            self.heapify(nums, maxIndex, lastIndex)
        return

if __name__ == "__main__":
    test = Solution()
    input = [3,9,5,10,6,7,7]
    # test.randomizedQuickSort(input, 0, len(input) - 1)
    # test.heapSort(input)
    input.sort()
    print(input)
    # print(test.mergeSort([8,5,7,9,10,1,3,2]))
    # test = [[0] * 3 for i in range(3)]
    # piles = [5,3,4,5]
    # memo = [[[-1 for i in range(len(piles))] for j in range(len(piles))]for z in range(2)]
    # print(test)
    # print(memo)
    # print(type(math.inf))