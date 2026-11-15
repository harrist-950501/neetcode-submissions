class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        mostContain = 0
        while r > l:
            height = min(heights[l], heights[r])
            contain = height * (r - l)
            mostContain = max(mostContain, contain)
            if heights[r] == height:
                r -= 1
            else:
                l += 1
        return mostContain