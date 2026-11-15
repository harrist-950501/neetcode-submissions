class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        lMax = 0
        rMax = 0
        totalW = 0
        while l <= r:
            if lMax < rMax:
                lMax = max(lMax, height[l])
                totalW += (lMax - height[l])
                l += 1
            else:
                rMax = max(rMax, height[r])
                totalW += (rMax - height[r])
                r -= 1
        return totalW

        