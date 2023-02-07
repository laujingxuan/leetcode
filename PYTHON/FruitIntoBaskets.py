class Solution:
    # time complexity O(N^2) with recursion solution. Non-ideal
    def totalFruitNonIdeal(self, fruits):
        maxCount = 0
        for i in range(len(fruits)):
            trackSet = set()
            maxCount = max(maxCount, self.checkCounts(fruits, i, trackSet))
        return maxCount


    def checkCounts(self, fruits, currentIndex, trackSet):
        if currentIndex >= len(fruits):
            return 0
        trackSet.add(fruits[currentIndex])
        if len(trackSet) > 2:
            return 0
        return self.checkCounts(fruits, currentIndex + 1, trackSet) + 1

    def totalFruit(self, fruits):
        if len(fruits) <= 2:
            return len(fruits)
        slow = 0
        fast = 0
        trackMap = {}
        currentFruitsType = set()
        maxFruits = 0
        while fast < len(fruits):
            if fast == 0 or fast != 0 and fruits[fast] != fruits[fast - 1]:
                trackMap[fruits[fast]] = fast
                if fruits[fast] not in currentFruitsType:
                    if len(currentFruitsType) == 2: 
                        maxFruits = max(maxFruits, fast-slow)
                        currentFruitsType.clear()
                        currentFruitsType.add(fruits[fast - 1])
                        slow = trackMap[fruits[fast - 1]]
                    currentFruitsType.add(fruits[fast])
            fast += 1
        maxFruits = max(maxFruits, fast - slow)
        return maxFruits
    
    #Easier understand but slightly worse time complexity than above due to need to loop slow one by one
    def totalFruitEasierUnderstand(self, fruits):
        trackMap = {}
        fast = 0
        slow = 0
        maxCount = 0
        while fast < len(fruits):
            count = trackMap.get(fruits[fast], 0)
            trackMap[fruits[fast]] = count + 1
            while len(trackMap) > 2:
                count = trackMap.get(fruits[slow])
                trackMap[fruits[slow]] -= 1
                if trackMap[fruits[slow]] == 0:
                    del trackMap[fruits[slow]]
                slow += 1
            maxCount = max(maxCount, fast - slow + 1)
            fast += 1
        return maxCount

    def totalFruitAnswer(self, tree):
        count, i = {}, 0
        for j, v in enumerate(tree):
            count[v] = count.get(v, 0) + 1
            if len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0: del count[tree[i]]
                i += 1
        print(j)
        print(i)
        return j - i + 1

if __name__ == "__main__":
    test = Solution()
    print(test.totalFruitAnswer([0,0,1,2]))