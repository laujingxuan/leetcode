import heapq

# Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.
# You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.
# Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.
# Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.
class Solution:
    #greedy method using maxHeap
    #time complexity is much better as at most O(Nlog(N)) due to the sorting and heapify
    def findMaximizedCapital(self, k, w, profits, capital):
        heap = []
        index =0 
        combi = sorted(zip(profits, capital), key = lambda x:x[1])
        for i in range(k):
            while index < len(combi) and combi[index][1] <= w:
                heapq.heappush(heap, -combi[index][0])
                index += 1
            if len(heap) == 0:
                return w
            w += -heapq.heappop(heap)
        return w


    # time limit exceeded non-ideal as time complexity is O(N^k)
    def findMaximizedCapital(self, k, w, profits, capital):
        capitalToProfitsMap = self.initGraph(profits, capital)
        hasVisitedProject = set()
        # print(capitalToProfitsMap)
        return self.getCapital(k, w, hasVisitedProject, capitalToProfitsMap, 0)
    
    def initGraph(self, profits, capital):
        capitalToProfitsMap = {}
        for i in range(len(profits)):
            profitsDetails = capitalToProfitsMap.get(capital[i], [])
            profitsDetails.append([i, profits[i]])
            capitalToProfitsMap[capital[i]] = profitsDetails
        return capitalToProfitsMap
    
    def getCapital(self, k, w, hasVisitedProject, capitalToProfitsMap, startIndex):
        if k == 0:
            return w
        maxCapital = w
        for i in range(startIndex, w + 1):
            # print(str(i) + "-" + str(w))
            availableProfits = capitalToProfitsMap.get(i, [])
            # print(availableProfits)
            for profit in availableProfits:
                if profit[0] in hasVisitedProject:
                    continue
                hasVisitedProject.add(profit[0])
                maxCapital = max(maxCapital, self.getCapital(k - 1, w + profit[1], hasVisitedProject, capitalToProfitsMap, i))
                hasVisitedProject.remove(profit[0])
        # print(str(w) + ":" + str(maxCapital))
        return maxCapital