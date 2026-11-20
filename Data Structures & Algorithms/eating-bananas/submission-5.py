class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxK = max(piles)
        l, r = 1, maxK

        while r > l:
            m = (l + r) // 2
            sumH = 0
            for pile in piles:
                sumH += (pile + m - 1) // m

            if sumH <= h:
                r = m
            else:
                l = m + 1

        return r
        