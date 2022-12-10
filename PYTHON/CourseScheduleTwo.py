class Solution:
    #a topological sort is a graph traversal in which each node v is visited only after all its dependencies are visited. A topological ordering is possible if and only if the graph has no directed cycles
    # time complexity of O(N + M) only since only needs to loop through the prerequisites once during graph initialization and space complexity of O(N) for the multiple list
    def findOrder(self, numCourses, prerequisites):
        coursesLinkCount = [0] * numCourses
        edgesTracking = [[] for i in range(numCourses)]
        self.initializeGraph(prerequisites, coursesLinkCount, edgesTracking)
        return self.solveByBFS(numCourses, coursesLinkCount, edgesTracking)

    def solveByBFS(self, numCourses, couresesLinkCount, edgesTracking):
        toVisitQueue = []
        for i in range(len(couresesLinkCount)):
            if couresesLinkCount[i] == 0:
                toVisitQueue.append(i)
        output = []
        while len(toVisitQueue) != 0:
            index = toVisitQueue.pop(0)
            output.append(index)
            relatedIndexes = edgesTracking[index]
            for ind in relatedIndexes:
                couresesLinkCount[ind] -= 1
                if couresesLinkCount[ind] == 0:
                    toVisitQueue.append(ind)
        if len(output) != numCourses:
            return []
        return output

    def initializeGraph(self, prerequisites, coursesLinkCount, edgesTracking):
        for i in range(len(prerequisites)):
            coursesLinkCount[prerequisites[i][0]] += 1
            edgesTracking[prerequisites[i][1]].append(prerequisites[i][0])
        return
    
    # not so smart way with time complexity of around O(N^2 + N*M)? ===> N is num of courses while m is length of prerequisites
    # space complexity of O(N) ===> use of set and multiple list
    def findOrderBad(self, numCourses, prerequisites):
        output = []
        hasVisited = set()
        preCoureseWithoutPreReq = []
        coursesWithoutPreReq = self.findCourseWithoutPreRequisites(numCourses, prerequisites, hasVisited)
        while coursesWithoutPreReq != preCoureseWithoutPreReq:
            print("coursesWithoutPreReq: " + str(coursesWithoutPreReq))
            for i in range(len(coursesWithoutPreReq)):
                if i not in hasVisited and coursesWithoutPreReq[i] == 0:
                    output.append(i)
                    hasVisited.add(i)
                    prerequisites = self.removeCoursesAdded(prerequisites, i)
                    print("prerequisites: " + str(prerequisites))
            preCoureseWithoutPreReq = coursesWithoutPreReq
            coursesWithoutPreReq = self.findCourseWithoutPreRequisites(numCourses, prerequisites, hasVisited)
        if len(output) != numCourses:
            return []
        return output
                

    def findCourseWithoutPreRequisites(self, numCourses, prerequisites, hasVisited):
        output = [0] * numCourses
        for i in range(len(prerequisites)):
            output[prerequisites[i][0]] += 1
        return output

    def removeCoursesAdded(self, prerequisites, num):
        output = []
        for i in range(len(prerequisites)):
            if prerequisites[i][1] != num:
                output.append(prerequisites[i])
        return output

if __name__ == "__main__":
    test = Solution()
    print(test.findOrder(2, [[1,0]]))
    # print(test.findOrder(4, [[0,1],[0,2],[1,3],[3,0]]))