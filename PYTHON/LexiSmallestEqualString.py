class Solution:

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        UF = {}
        for i in range(len(s1)):
            self.union(s1[i], s2[i], UF)
        output = ""
        for i in range(len(baseStr)):
            output += self.find(baseStr[i], UF)
        return output

    def find(self, x, UF):
        if x not in UF:
            UF[x] = x
        if UF[x] != x:
            return self.find(UF[x], UF)
        return UF[x]
    
    def union(self, x, y, UF):
        rootX = self.find(x, UF)
        rootY = self.find(y, UF)
        if rootX > rootY:
            UF[rootX] = rootY
        else:
            UF[rootY] = rootX
        return

    def smallestEquivalentStringNotSoIdeal(self, s1: str, s2: str, baseStr: str) -> str:
        trackMap = {}
        for i in range(len(s1)):
            str1List = trackMap.get(s1[i], [])
            str2List = trackMap.get(s2[i], [])
            str1List.append(s2[i])
            str2List.append(s1[i])
            trackMap[s1[i]] = str1List
            trackMap[s2[i]] = str2List
        
        output = ""
        stack = []
        for i in range(len(baseStr)):
            if baseStr[i] in trackMap:
                stack += trackMap[baseStr[i]]
            smallestLexi = baseStr[i]
            hasVisited = set()
            hasVisited.add(baseStr[i])
            while len(stack) > 0:
                currentChar = stack.pop()
                if currentChar in hasVisited:
                    continue
                hasVisited.add(currentChar)
                if currentChar < smallestLexi:
                    smallestLexi = currentChar
                stack += trackMap[currentChar]
            output += smallestLexi
        return output