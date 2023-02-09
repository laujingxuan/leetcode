class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        ideaMap = {}
        for i in range(len(ideas)):
            found = ideaMap.get(ideas[i][0], set())
            found.add(ideas[i][1:])
            ideaMap[ideas[i][0]] = found

        count = 0
        for key1 in ideaMap:
            for key2 in ideaMap:
                if key1 <= key2:
                    continue
                k = len(ideaMap[key1] & ideaMap[key2]) # Number of duplicated suffixes as & find intersection of both sets! Its a set operation
                count += 2 * (len(ideaMap[key1]) - k) * (len(ideaMap[key2]) - k)
        return count