class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        count = 0
        prev = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[prev][1]:
                if intervals[i][1] <= intervals[prev][1]:
                    prev = i
                count += 1
            else:
                prev = i

        return count