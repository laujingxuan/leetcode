from collections import Counter


class Solution:
    def countSubTrees(self, n, edges, labels):
        edgesMap = {}
        for edge in edges:
            nodeList1 = edgesMap.get(edge[0],[])
            nodeList2 = edgesMap.get(edge[1],[])
            nodeList1.append(edge[1])
            nodeList2.append(edge[0])
            edgesMap[edge[0]] = nodeList1
            edgesMap[edge[1]] = nodeList2
        output = [0]*n
        self.countSubDFS(edgesMap, output, labels, -1, 0)
        return output

    def countSubDFS(self, edgesMap, output, labels, parent, currentNode):
        cnt = Counter()
        cnt[labels[currentNode]] += 1
        subNodes = edgesMap[currentNode]
        for node in subNodes:
            if node != parent:
                cnt += self.countSubDFS(edgesMap, output, labels, currentNode, node)
        output[currentNode] = cnt[labels[currentNode]]
        return cnt

    def countSubDFSWithoutCounter(self, edgesMap, output, labels, hasVisited, rootNode):
        cnt = [0] * 26
        if rootNode not in hasVisited:
            cnt[ord(labels[rootNode]) - ord('a')] += 1
            print(cnt)
            hasVisited.add(rootNode)
            subNodes = edgesMap[rootNode]
            for node in subNodes:
                returnedCount = self.countSubDFSWithoutCounter(edgesMap, output, labels, hasVisited, node)
                for i in range(len(returnedCount)):
                    cnt[i] += returnedCount[i]
            output[rootNode] = cnt[ord(labels[rootNode]) - ord('a')]
        return cnt

if __name__ == "__main__":
    test = Solution()
    print(test.countSubTrees(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], "abaedcd"))