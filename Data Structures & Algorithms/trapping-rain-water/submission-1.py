class Solution:
    def trap(self, height: List[int]) -> int:
        thl = [0] * len(height) # tallest height on my left
        thr = [0] * len(height) # tallest height on my right

        th = 0 # tallest height
        for i, h in enumerate(height):
            thl[i] = th
            th = max(th, h)

        th = 0
        for i in reversed(range(len(height))):
            thr[i] = th
            th = max(th, height[i])

        totalWater = 0
        for i, h in enumerate(height):
            totalWater += max(0, min(thl[i], thr[i]) - h)

        return totalWater

        