class Solution:
    def lexicalOrder(self, n):
        output = []
        for i in range(1,10):
            self.dfs(i, n, output)
        return output
        
    def dfs(self, current, n, output):
        if current > n:
            return
        output.append(current)
        for i in range(10):
            self.dfs(current*10 + i, n, output)
        return