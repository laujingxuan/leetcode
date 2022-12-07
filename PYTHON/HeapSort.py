def heapify(arr, rootIndex, lastIndex):
    leftNode = (2 * rootIndex) + 1
    rightNode = (2* rootIndex) + 2
    maxIndex = rootIndex
    if leftNode < lastIndex and arr[leftNode] > arr[maxIndex]:
        maxIndex = leftNode
    if rightNode < lastIndex and arr[rightNode] > arr[maxIndex]:
        maxIndex = rightNode
    if rootIndex != maxIndex:
        arr[maxIndex], arr[rootIndex] = arr[rootIndex], arr[maxIndex]
        heapify(arr, maxIndex, lastIndex)

def HeapSort(arr):
    arrayLen = len(arr)
    # Starts from (arrayLen-1)/2 because we only need to heapify the parent node (with child node)
    for rootIndex in range((arrayLen-1)//2, -1, -1):
        heapify(arr, rootIndex, arrayLen)
    # then we keep on swapping the lastIndex with the largestVal, which is index 0. and heapify the array again (exclude the swapped last index)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)

if __name__ =="__main__":
    arr = [3,7,1,4,7,8]
    HeapSort(arr)
    print(arr)