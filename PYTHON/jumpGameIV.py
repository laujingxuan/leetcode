# Given an array of integers arr, you are initially positioned at the first index of the array.

# In one step you can jump from index i to index:

# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
# Return the minimum number of steps to reach the last index of the array.

# Notice that you can not jump outside of the array at any time.

class Solution:
    def minJumpsAlmostTimeLimitExceeded(self, arr):
        indexMap = {}
        self.initGraph(arr, indexMap)
        queue = [0]
        hasVisited = set()
        numberOfSteps = 0
        while len(queue) > 0:
            queueLen = len(queue)
            for i in range(queueLen):
                currIndex = queue.pop(0)
                if currIndex in hasVisited or currIndex < 0 or currIndex >= len(arr):
                    continue
                hasVisited.add(currIndex)
                if currIndex == len(arr) - 1:
                    return numberOfSteps
                #append index of duplicated value
                arrayList = indexMap.pop(arr[currIndex], [])
                queue += arrayList
                #append before and after
                queue.append(currIndex - 1)
                queue.append(currIndex + 1)
            numberOfSteps += 1
        return -1


    def initGraph(self, arr, indexMap):
        for i in range(len(arr) - 1, -1 , -1):
            arrayList = indexMap.get(arr[i], [])
            arrayList.append(i)
            indexMap[arr[i]] = arrayList
        return