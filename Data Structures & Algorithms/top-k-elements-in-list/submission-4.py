class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToCount = {}
        for num in nums:
            numToCount[num] = numToCount.get(num, 0) + 1
        
        buckets = [[] for _ in range(1 + len(nums))]
        for num in numToCount:
            buckets[numToCount[num]].append(num)
        
        output = []
        for bucket in buckets[::-1]:
            output.extend(bucket)
            if len(output) == k:
                return output
         