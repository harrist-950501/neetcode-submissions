class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToCount = {}
        for num in nums:
            numToCount[num] = numToCount.get(num, 0) + 1
        
        return sorted(numToCount, key=numToCount.get, reverse=True)[:k]
         