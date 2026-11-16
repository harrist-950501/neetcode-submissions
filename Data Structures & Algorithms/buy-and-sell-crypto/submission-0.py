class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        BBP = prices[0] #best buying price so far
        for price in prices:
            maxP = max(maxP, price - BBP)
            BBP = min(BBP, price)

        return maxP