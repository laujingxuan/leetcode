class Solution:

    def longestCycle(self, edges):
        hasVisited = set()
        maxCycleLen = -1
        for i in range(len(edges)):
            cycleLen = self.checkCycle(edges, i, hasVisited, 0, {})
            maxCycleLen = max(maxCycleLen, cycleLen)
        return maxCycleLen

    def checkCycle(self, edges, index, hasVisited, counter, counterMap):
        if index in counterMap:
            return counter - counterMap[index]
        if index in hasVisited:
            return -1
        hasVisited.add(index)
        counterMap[index] = counter
        newIndex = edges[index]
        if newIndex == -1:
            return -1
        return self.checkCycle(edges, newIndex, hasVisited, counter + 1, counterMap)

    ## not ideal
    def longestCycleTimeLimitExceeded(self, edges):
        trackMap = {}
        for i in range(len(edges)):
            if edges[i] == -1:
                continue
            trackMap[i] = edges[i]
        hasVisited = set()
        maxCycleLen = -1
        for i in range(len(edges)):
            if i in hasVisited:
                continue
            cycleLen = self.checkCycleTimeLimit(trackMap, i, hasVisited)
            maxCycleLen = max(maxCycleLen, cycleLen)
        return maxCycleLen

    def checkCycleTimeLimit(self, trackMap, index, hasVisited):
        checkSet = set()
        if index not in trackMap:
            return -1
        dest = trackMap[index]
        cycleLen = 1
        while dest != index:
            if dest in checkSet:
                return -1
            if dest not in trackMap:
                hasVisited.update(checkSet)
                return -1
            checkSet.add(dest)
            dest = trackMap[dest]
            cycleLen += 1
        hasVisited.update(checkSet)
        return cycleLen
