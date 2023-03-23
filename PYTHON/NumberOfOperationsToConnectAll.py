# There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

# You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

# Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        connectionSetList = [set() for i in range(n)]
        #use map here also can. same concept
        for connection in connections:
            connectionSetList[connection[0]].add(connection[1])
            connectionSetList[connection[1]].add(connection[0])

        hasVisited = set()
        cableNeeded = 0
        for i in range(n):
            cableNeeded += self.dfsHelper(i, connectionSetList, hasVisited)
        return cableNeeded - 1

    def dfsHelper(self, index, connectionSetList, hasVisited):
        if index in hasVisited:
            return 0
        hasVisited.add(index)
        # print(index)
        for node in connectionSetList[index]:
            self.dfsHelper(node, connectionSetList, hasVisited)
        return 1
