class Solution:
    def canVisitAllRoomsBFS(self, rooms):
        if len(rooms) <= 1:
            return True
        hasVisited = set()
        hasVisited.add(0)
        queue = []
        queue.append(rooms[0])
        while len(queue) > 0:
            keys = queue.pop(0)
            for key in keys:
                if key not in hasVisited:
                    queue.append(rooms[key])
                    hasVisited.add(key)
        return len(hasVisited) == len(rooms)

    def canVisitAllRoomsDFS(self, rooms):
        if len(rooms) <= 1:
            return True
        visitedMemo = [False for i in range(len(rooms))]
        visitedMemo[0] = True
        self.canVisitDFS(rooms, visitedMemo, 0)
        for i in range(len(visitedMemo)):
            if visitedMemo[i] == False:
                return False
        return True

    def canVisitDFS(self, rooms, visitedMemo, currentRoom):
        keys = rooms[currentRoom]
        for key in keys:
            if visitedMemo[key] == False:
                visitedMemo[key] = True
                self.canVisitDFS(rooms, visitedMemo, key)
        return