class Solution:
# You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.
# For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.
# Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0
        routesTrack = {}
        hasVisited = set()
        queue = []
        # Create a map of busStop as key and the list of buses that stop at the bus stop as value
        # If the bus stop is the source bus stop, add the bus stop to the queue as these bus stops will be our starting points
        # Use hasVisited to keep track of the busses that we have checked/added in the queue
        for i in range(len(routes)):
            for stop in routes[i]:
                if stop in routesTrack:
                    routesTrack[stop].append(i)
                else:
                    routesTrack[stop] = [i]
                if stop == source:
                    hasVisited.add(i)
                    queue.append(i)
        # print(routesTrack)
        # print(len(queue))
        minimumNumberOfBuses = 0
        while len(queue) > 0:
            minimumNumberOfBuses += 1
            # loop through queue. 
            # If target bus stop is found in any of the path of the buses, return the minimum number of buses. Else, add the buses that stop at the bus stop to the queue
            queueLen = len(queue)
            for i in range(queueLen):
                current = queue.pop(0)
                for j in range(len(routes[current])):
                    if routes[current][j] == target:
                        return minimumNumberOfBuses
                    if routes[current][j] in routesTrack:
                        # print(routes[current][j])
                        # print(routesTrack[routes[current][j]])
                        relatedRoutes = routesTrack[routes[current][j]]
                        for relatedRouteIndex in range(len(relatedRoutes)):
                            if relatedRoutes[relatedRouteIndex] not in hasVisited:
                                queue.append(relatedRoutes[relatedRouteIndex])
                                hasVisited.add(relatedRoutes[relatedRouteIndex])
            print(queue)
        return -1

if __name__ == "__main__":
    test = Solution()
    print(test.numBusesToDestination([[1,2,7],[3,6,7]], 1, 6))
    print(test.numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12))