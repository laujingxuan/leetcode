class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Need to sort the intervals first by the first element
        self.quickSort(intervals, 0, len(intervals) - 1)
        output = []
        i = 1
        while i < len(intervals):
            if intervals[i-1][1] < intervals[i][0]:
                output.append(intervals[i-1])
            else:
                intervals[i - 1] = [min(intervals[i-1][0], intervals[i][0]),max(intervals[i-1][1], intervals[i][1])]
                intervals[i] = intervals[i - 1]
            i += 1
        output.append(intervals[-1])
        return output

    def quickSort(self, intervals, start, end):
        if end - start <=0:
            return
        target = intervals[end]
        j = start
        for i in range(start, end):
            if target[0] > intervals[i][0]:
                intervals[i], intervals[j] = intervals[j], intervals[i]
                j += 1
        intervals[end], intervals[j] = intervals[j], intervals[end]
        self.quickSort(intervals, start, j - 1)
        self.quickSort(intervals, j + 1, end)
        return
