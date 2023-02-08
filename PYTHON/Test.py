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

    def partition(self, nums, left, right):
        #randomization
        randomIndex = random.randrange(left, right + 1)
        nums[randomIndex], nums[right] = nums[right], nums[randomIndex]
        targetVal = nums[right]
        i = left
        index = left
        while index < right:
            if nums[index] <= targetVal:
                nums[i], nums[index] = nums[index], nums[i]
                i += 1
            index += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i


    def randomizedQuickSort(self, nums, left, right):
        if right > left:
            pivot = self.partition(nums, left, right)
            self.randomizedQuickSort(nums, pivot + 1, right)
            self.randomizedQuickSort(nums, left, pivot - 1)
        return

    def heapify(self, nums, index, right):
        leftChildIndex = 2 * index + 1
        rightChildIndex = 2 * index + 2
        maxIndex = index
        if leftChildIndex <= right and nums[leftChildIndex] > nums[maxIndex]:
            maxIndex = leftChildIndex
        if rightChildIndex <= right and nums[rightChildIndex] > nums[maxIndex]:
            maxIndex = rightChildIndex
        if maxIndex != index:
            nums[maxIndex], nums[index] = nums[index], nums[maxIndex]
            self.heapify(nums, maxIndex, right)
        return

    def heapSort(self, nums):
        for i in range((len(nums)-2)//2, -1, -1):
            self.heapify(nums, i, len(nums) - 1)

        for i in range(len(nums)-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, 0, i - 1)
        return

    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        midIndex = len(nums)//2
        leftSorted = self.mergeSort(nums[:midIndex])
        rightSorted = self.mergeSort(nums[midIndex:])

        output = []
        leftIndex = 0
        rightIndex = 0

        while leftIndex < len(leftSorted) and rightIndex < len(rightSorted):
            if leftSorted[leftIndex] > rightSorted[rightIndex]:
                output.append(rightSorted[rightIndex])
                rightIndex += 1
            else:
                output.append(leftSorted[leftIndex])
                leftIndex += 1
        output += leftSorted[leftIndex:] + rightSorted[rightIndex:]
        print(output)
        return output

    def binarySearch(self, nums, target):
        nums.sort()
        left = 0
        right = len(nums) - 1
        while right >= left:
            print(str(left) + ":" + str(right))
            midIndex = (right+left)//2
            if nums[midIndex] == target:
                return True
            if nums[midIndex] > target:
                right = midIndex - 1
            else:
                left = midIndex + 1
        return False


if __name__ == "__main__":
    test = Solution()
    input = [3,9,5,10,6,7,7,1]
    # test.randomizedQuickSort(input, 0, len(input) - 1)
    # test.heapSort(input)
    # print(input)
    # print(test.mergeSort(input))
    print(test.binarySearch(input, 3))
    # print(test.mergeSort([8,5,7,9,10,1,3,2]))
    # test = [[0] * 3 for i in range(3)]
    # piles = [5,3,4,5]
    # memo = [[[-1 for i in range(len(piles))] for j in range(len(piles))]for z in range(2)]
    # print(test)
    # print(memo)
    # print(type(math.inf))