class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0] * n

        def climb(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if ways[i] != 0:
                return ways[i]
            ways[i] = climb(i + 1) + climb(i + 2)
            return ways[i]

        return climb(0)
        