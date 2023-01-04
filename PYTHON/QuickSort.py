# https://www.geeksforgeeks.org/quick-sort/
import random


def partition(arr, low, high):
    i = low
    pivot = arr[high]
    for j in range(low, high):
        if pivot > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, pivot + 1, high)
        quickSort(arr, low, pivot - 1)
    return arr

def partitionAlt(array, low, high):
    #to randomized the number
    randomNumber = random.randrange(low, high+1)
    array[randomNumber], array[high] = array[high], array[randomNumber]

    anchor = array[high]
    smallerIndex = low
    for i in range(low, high):
        if array[i] <= anchor:
            array[smallerIndex], array[i] = array[i], array[smallerIndex]
            smallerIndex += 1
    array[smallerIndex], array[high] = array[high], array[smallerIndex]
    return smallerIndex


def randomizedQuickSort(array, low, high):
    if high > low:
        index = partitionAlt(array, low, high)
        randomizedQuickSort(array, low, index - 1)
        randomizedQuickSort(array, index + 1, high)
    return array

if __name__ == "__main__":
    print(quickSort([7,4,6,1,3], 0, 4))
    print(randomizedQuickSort([7,4,6,1,3], 0, 4))