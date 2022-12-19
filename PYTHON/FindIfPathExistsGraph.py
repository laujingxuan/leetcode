class Solution:
    def validPath(self, n, edges, source, destination):
        if source == destination:
            return True        
        hasVisited = set()
        queue = []
        edgesMap = {}
        for i in range(len(edges)):
            if edges[i][0] == source or edges[i][1] == source:
                queue.append(edges[i])
            self.addToEdgeMap(edgesMap, edges[i][0], edges[i])
            self.addToEdgeMap(edgesMap, edges[i][1], edges[i])
        hasVisited.add(source)
        while len(queue) > 0:
            current = queue.pop(0)
            if current[0] == destination or current[1] == destination:
                return True
            if current[0] not in hasVisited and edgesMap[current[0]] != None:
                queue = queue + edgesMap[current[0]]
                hasVisited.add(current[0])
            if current[1] not in hasVisited and edgesMap[current[1]] != None:
                queue = queue + edgesMap[current[1]]
                hasVisited.add(current[1])
        return False  

    def addToEdgeMap(self, edgesMap, key, edge):
        if key in edgesMap:
            edgesMap[key].append(edge)
        else:
            edgesMap[key] = [edge]  

    def validPathSimplified(self, n, edges, source, destination):
        if source == destination:
            return True        
        hasVisited = set()
        queue = []
        edgesMap = {}
        for i in range(len(edges)):
            if edges[i][0] == source:
                queue.append(edges[i][1])
            if edges[i][1] == source:
                queue.append(edges[i][0])
            self.addToEdgeMapSimplified(edgesMap, edges[i][0], edges[i][1])
            self.addToEdgeMapSimplified(edgesMap, edges[i][1], edges[i][0])
        hasVisited.add(source)
        while len(queue) > 0:
            current = queue.pop(0)
            if current == destination:
                return True
            if current not in hasVisited and edgesMap[current] != None:
                queue = queue + edgesMap[current]
                hasVisited.add(current)
        return False   

    def addToEdgeMapSimplified(self, edgesMap, key, value):
        if key in edgesMap:
            edgesMap[key].append(value)
        else:
            edgesMap[key] = [value]


if __name__ == "__main__":
    test = Solution()
    print(test.validPath(6, [[0,1],[1,2],[2,0]], 0, 2))
    print(test.validPathSimplified(6, [[0,1],[1,2],[2,0]], 0, 2))
    # print(test.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))
