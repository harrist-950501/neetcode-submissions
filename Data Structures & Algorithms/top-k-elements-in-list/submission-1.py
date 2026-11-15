from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = Counter(nums)
        output = []
        for num, _ in numCount.most_common(k):
            output.append(num)
        return output