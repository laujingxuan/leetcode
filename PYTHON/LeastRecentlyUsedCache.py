class LinkNode:
    def __init__(self, key, value, next = None, previous = None):
        self.key = key
        self.value = value
        self.next = next
        self.previous = previous

class LRUCache:
    def __init__(self, capacity: int):
        # key of map is key; value of map is linkNode
        self.trackMap = {}
        self.capacity = capacity
        self.latestNode = LinkNode(0,0)
        self.earliestNode = LinkNode(0,0)
        self.earliestNode.next = self.latestNode
        self.latestNode.previous = self.earliestNode

    def get(self, key: int) -> int:
        if key in self.trackMap:
            node = self.trackMap[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.trackMap:
            self._remove(self.trackMap[key])
        n = LinkNode(key, value)
        self._add(n)
        self.trackMap[key] = n
        if len(self.trackMap) > self.capacity:
            n = self.earliestNode.next
            self._remove(n)
            del self.trackMap[n.key]

    def _remove(self, node):
        p = node.previous
        n = node.next
        p.next = n
        n.previous = p

    def _add(self, node):
        p = self.latestNode.previous
        p.next = node
        self.latestNode.previous = node
        node.previous = p
        node.next = self.latestNode

if __name__ == "__main__":
    test = LRUCache(3)
    test.put(1,1)
    test.put(2,2)
    # print(test.latestNode.previous.next.value)
    test.put(3,3)
    test.put(4,4)
    print(test.get(4))
    # print(test.latestNode.previous.previous.value)
    print(test.get(3))
    print(test.get(2))
    print(test.get(1))
    test.put(5,5)
    print(test.get(1))
    print(test.get(2))
    print(test.get(3))
    print(test.get(4))
    print(test.get(5))
