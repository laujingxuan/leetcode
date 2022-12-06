class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        checkMap = {}
        highestCountTask = 1
        totalTasks = len(tasks)
        for task in tasks:
            if task in checkMap:
                checkMap[task] += 1
            else:
                checkMap[task] = 1
            highestCountTask = max(highestCountTask, checkMap[task])
        highCount = 0
        for key in checkMap:
            if checkMap[key] == highestCountTask:
                highCount += 1
        if (highestCountTask - 1) * (n + 1) + highCount > totalTasks:
            return (highestCountTask - 1) * (n + 1) + highCount
        return totalTasks
