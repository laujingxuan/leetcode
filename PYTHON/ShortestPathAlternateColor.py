import math


class Solution:
    #better time complexity then below as only need to BFS from 0 once. Hence time complexity O(2*N) ==> Only need to scan through the graph twice for red path and blue path on each possibility
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        graph = self.buildGraphs(n, redEdges, blueEdges)
        queue = []
        #second value is the color
        queue.append([0, 1])
        queue.append([0, -1])
        output = [math.inf] * n
        output[0] = 0

        hasVisited = set()
        stepsNeeded = 0
        while len(queue) > 0:
            queueLen = len(queue)
            stepsNeeded += 1
            for i in range(queueLen):
                curr = queue.pop(0)
                node = curr[0]
                color = curr[1]
                oppColor = -color
                for j in range(1, n):
                    if graph[node][j] == oppColor or graph[node][j] == 0:
                        key = str(j) + ":" + str(oppColor)
                        if key in hasVisited:
                            continue
                        hasVisited.add(key)
                        queue.append([j, oppColor])
                        output[j] = min(output[j], stepsNeeded)
        for i in range(1, n):
            if output[i] == math.inf:
                output[i] = -1

        return output
                

    def buildGraphs(self, n, redEdges, blueEdges):
        graph = [[-n for j in range(n)] for i in range(n)]

        #1 means red path
        for edge in redEdges:
            graph[edge[0]][edge[1]] = 1
        #-1 means blue path
        for edge in blueEdges:
            if graph[edge[0]][edge[1]] == 1:
                graph[edge[0]][edge[1]] = 0
            else:
                graph[edge[0]][edge[1]] = -1
        return graph


    #worse time complexity O(2*N^2) as might need to BFS once from 0 for every nodes and for both red and blue path
    def shortestAlternatingPathsNonIdeal(self, n, redEdges, blueEdges):
        blueMap={}
        redMap={}
        for edge in redEdges:
            dest = redMap.get(edge[0], [])
            dest.append([edge[1], 1])
            redMap[edge[0]] = dest

        for edge in blueEdges:
            dest = blueMap.get(edge[0], [])
            dest.append([edge[1], -1])
            blueMap[edge[0]] = dest

        output = [0]
        for i in range(1, n):
            queue = []
            queue += redMap.get(0, [])
            queue += blueMap.get(0, [])
            stepsNeeded = self.findPath(redMap, blueMap, i, queue)
            output.append(stepsNeeded)
        return output

    def findPath(self, redMap, blueMap, target, queue):
        if len(queue) == 0:
            return -1
        stepsNeeded = 1
        hasVisited = set()
        while len(queue) != 0:
            queueLen = len(queue)
            for i in range(queueLen):
                combi = queue.pop(0)
                dest = combi[0]
                color = combi[1]
                key = str(color) + ":" + str(dest)
                if key in hasVisited:
                    continue
                hasVisited.add(key)
                if dest == target:
                    return stepsNeeded
                if color == 1:
                    queue += blueMap.get(dest, [])
                else:
                    queue += redMap.get(dest, [])
            stepsNeeded += 1
        return -1
