# https://www.geeksforgeeks.org/quick-sort/
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

if __name__ == "__main__":
    print(quickSort([7,4,6,1,3], 0, 4))