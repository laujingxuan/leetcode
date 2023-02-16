class Solution:
    def simplifyPath(self, path: str) -> str:
        outputStack = []
        splitList = path.split("/")
        
        for elem in splitList:
            if len(elem) == 0 or elem == ".":
                continue
            if elem == "..":
                if len(outputStack) != 0:
                    outputStack.pop()
                continue
            outputStack.append(elem)

        output = ""
        for elem in outputStack:
            output += "/" + elem
        
        if output == "":
            return "/"
        return output
