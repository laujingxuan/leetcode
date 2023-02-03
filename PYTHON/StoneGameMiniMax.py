class Solution:
    #Exceed time limit for certain test cases
    def stoneGameNonIdeal(self, piles):
        total = 0
        for i in range(len(piles)):
            total += piles[i]

        if self.stoneGameHelper(piles, total, piles[0], 1, len(piles) - 1):
            return True
        return self.stoneGameHelper(piles, total, piles[len(piles)-1], 0, len(piles) - 2)

    def stoneGameHelper(self, piles, total, current, startIndex, lastIndex):
        if current > total//2:
            return True
        if lastIndex - startIndex <= 0:
            return False
        #if Bob takes first
        firstStartInd = startIndex + 1
        if self.stoneGameHelper(piles, total, current + piles[firstStartInd], firstStartInd + 1, lastIndex):
            return True
        if self.stoneGameHelper(piles, total, current + piles[lastIndex], firstStartInd, lastIndex - 1):
            return True            
        #if Bob takes last
        secondLastInd = lastIndex - 1
        if self.stoneGameHelper(piles, total, current + piles[secondLastInd], startIndex, secondLastInd - 1):
            return True
        if self.stoneGameHelper(piles, total, current + piles[startIndex], startIndex + 1, secondLastInd):
            return True
        return False

    def stoneGameUsingDP(self, piles):
        memo = [[[-1 for i in range(len(piles))] for j in range(len(piles))]for z in range(2)]
        #Alice is playerId 0 while bob is playerId 1
        endScore = self.stoneGameHelper(piles, 0, len(piles) - 1, 0, memo) 
        return endScore > 0

    def stoneGameHelper(self, piles, startIndex, lastIndex, playerId, memo):
        if lastIndex < startIndex:
            return 0
        if memo[playerId][startIndex][lastIndex] > -1:
            return memo[playerId][startIndex][lastIndex]
        nextPlayerId = abs(playerId - 1)
        if playerId == 0:
            #maximize the score
            memo[playerId][startIndex][lastIndex] = max(self.stoneGameHelper(piles, startIndex + 1, lastIndex, nextPlayerId, memo)+ piles[startIndex], self.stoneGameHelper(piles, startIndex, lastIndex - 1, nextPlayerId, memo)+piles[lastIndex])
        else:
            #minimize the score
            memo[playerId][startIndex][lastIndex] = min(self.stoneGameHelper(piles, startIndex + 1, lastIndex, nextPlayerId, memo) - piles[startIndex], self.stoneGameHelper(piles, startIndex, lastIndex - 1, nextPlayerId, memo)- piles[lastIndex])
        return memo[playerId][startIndex][lastIndex]

if __name__ == "__main__":
    test = Solution()
    piles = [5,3,4,5]
    print(test.stoneGameUsingMemo(piles))