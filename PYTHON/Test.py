class Solution:
    def quickSort(self, input, low, high):
        if len(input) == 0 or high - low <= 0:
            return
        toCompare = input[high]
        i = low
        changeIndex = low
        while i < high:
            if input[i] <= toCompare:
                input[changeIndex], input[i] = input[i], input[changeIndex]
                changeIndex += 1
            i += 1
        input[changeIndex], input[high] = input[high], input[changeIndex]
        self.quickSort(input, low, changeIndex - 1)
        self.quickSort(input, changeIndex + 1, high)
        return

    def heapify(self, array, currentIndex, lastIndex):
        maxIndex = currentIndex
        if 2 * currentIndex + 1 <= lastIndex and array[2*currentIndex + 1] > array[maxIndex]:
            maxIndex = 2 * currentIndex + 1
        if 2 * currentIndex + 2 <= lastIndex and array[2*currentIndex + 2] > array[maxIndex]:
            maxIndex = 2 * currentIndex + 2
        if maxIndex != currentIndex:
            array[currentIndex], array[maxIndex] = array[maxIndex], array[currentIndex]
            self.heapify(array, maxIndex, lastIndex)
        return

    def heapSort(self, input):
        for i in range(len(input) - 1, -1, -1):
            self.heapify(input, i, len(input) - 1)
        index = len(input) - 1
        while index > 0:
            input[index], input[0] = input[0], input[index]
            index -= 1
            self.heapify(input, 0, index)
        return input


if __name__ == "__main__":
    # test = Solution()
    # input = [3,9,5,10,6,7,7]
    # test.quickSort(input, 0, len(input) - 1)
    # test.heapSort(input)
    # print(input)

    # for i in range(2,3):
    #     print(i)
    test = [1]
    print(test)
    del test[-1]
    print(test)