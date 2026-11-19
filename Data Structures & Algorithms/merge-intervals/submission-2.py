class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []

        for cur in intervals:
            if not merged or cur[0] > merged[-1][1]:
                merged.append(cur.copy())
            else:
                merged[-1][1] = max(merged[-1][1], cur[1])
            
        return merged