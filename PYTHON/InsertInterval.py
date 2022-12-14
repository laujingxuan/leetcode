# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

class Solution:
    def insertDirtyMethod(self, intervals, newInterval):
        insertedStartIndex = -1
        for i in range(len(intervals)):
            if intervals[i][1] >= newInterval[0]:
                if i == 0 and intervals[i][0] > newInterval[1]:
                    return [newInterval] + intervals
                insertedStartIndex = i
                if intervals[i][0] > newInterval[1]:
                    return intervals[:insertedStartIndex] + [newInterval] + intervals[insertedStartIndex:]
                break
        if insertedStartIndex == -1:
            intervals.append(newInterval)
            return intervals
        insertedEndIndex = -1
        for i in range(insertedStartIndex + 1, len(intervals)):
            if intervals[i][0] > newInterval[1]:
                insertedEndIndex = i - 1
                break
        if insertedEndIndex == -1:
            return intervals[:insertedStartIndex] + [[min(intervals[insertedStartIndex][0], newInterval[0]), max(intervals[insertedEndIndex][1], newInterval[1])]]
        return intervals[:insertedStartIndex] + [[min(intervals[insertedStartIndex][0], newInterval[0]), max(intervals[insertedEndIndex][1], newInterval[1])]] + intervals[insertedEndIndex + 1:]
    
    def insert(self, intervals, newInterval):
        output = []
        i = 0
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            output.append(intervals[i])
            i += 1
        print(output)
        print(i)
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        return output + [newInterval] + intervals[i:]

if __name__ =="__main__":
    test = Solution()
    # print(test.insert([[1,5]], [0,0]))
    # print(test.insert([[0,10],[14,14],[15,20]], [11,11]))
    print(test.insert([[1,5], [4,7]], [2,3]))
    # print(test.insert([[1,3],[6,9]], [2,5]))
    # print(test.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))