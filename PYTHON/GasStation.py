class Solution:
    #time complexity O(N)
    #space complexity O(1)
    def canCompleteCircuit(self, gas, cost):
        tank = 0
        start = 0
        netTotalGasAndCost = 0
        for i in range(len(gas)):
            netTotalGasAndCost += gas[i] - cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        if start >= len(gas) or netTotalGasAndCost < 0:
            return -1
        return start


    #Time limit exceeded. Non Ideal
    #time complexity O(N^2) if every gas>cost except the very last one which is very big cost
    #space complexity = O(1)
    def canCompleteCircuitTimeLimitedExceeded(self, gas, cost) -> int:
        for i in range(len(gas)):
            if gas[i] >= cost[i]:
                if self.checkCanComplete(gas[i:]+gas[:i], cost[i:]+cost[:i]):
                    return i
        return -1

    def checkCanComplete(self, gas, cost):
        currentGas = 0
        for i in range(len(gas)):
            currentGas += gas[i] - cost[i]
            if currentGas < 0:
                return False
        return True