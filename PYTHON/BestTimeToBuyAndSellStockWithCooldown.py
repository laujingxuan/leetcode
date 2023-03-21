class Solution:
    
    #without array/cache used, more complicated
    def maxProfitBest(self, prices):
        if len(prices) < 2:
            return 0
        
        prevMaxBuy = 0
        currentMaxBuy = -prices[0]
        currentMaxSell = 0
        prevMaxSell = 0

        for price in prices:
            prevMaxBuy = currentMaxBuy
            currentMaxBuy = max(prevMaxSell - price ,prevMaxBuy)
            prevMaxSell = currentMaxSell
            currentMaxSell = max(prevMaxBuy + price ,prevMaxSell)

        return currentMaxSell

    def maxProfitWithArray(self, prices):
        if len(prices) < 2:
            return 0
        
        buyMaxProfit = [0 for i in range(len(prices))]
        sellMaxProfit = [0 for i in range(len(prices))]

        for i in range (len(prices)):
            if i == 0:
                buyMaxProfit[i] = - prices[i]
                continue
            if i == 1:
                buyMaxProfit[i] = max(buyMaxProfit[i - 1], -prices[i])
                sellMaxProfit[i] = max(sellMaxProfit[i - 1], buyMaxProfit[i - 1] + prices[i])
                continue
            buyMaxProfit[i] = max(buyMaxProfit[i - 1], sellMaxProfit[i - 2] - prices[i])
            sellMaxProfit[i] = max(sellMaxProfit[i - 1], buyMaxProfit[i - 1] + prices[i])
        return sellMaxProfit[-1]

    def maxProfitTimeLimitExceeded(self, prices: List[int]) -> int:
        memo = [[-1 for i in range(len(prices))] for j in range(len(prices))]
        return self.findMaxProfit(prices, 0, memo)

    def findMaxProfit(self, prices, startIndex, memo):
        if startIndex >= len(prices):
            return 0
        maxProfit = 0
        for buyIndex in range(startIndex, len(prices)):
            for sellIndex in range(buyIndex + 1, len(prices)):
                profit = 0
                if memo[buyIndex][sellIndex] != -1:
                    profit = memo[buyIndex][sellIndex]
                else:
                    profit = prices[sellIndex] - prices[buyIndex] + self.findMaxProfit(prices, sellIndex + 2, memo)
                    memo[buyIndex][sellIndex] = profit
                maxProfit = max(maxProfit, profit)
        return maxProfit
