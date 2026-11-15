class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            target -= num
            for j in range(i + 1, len(nums)):
                if target - nums[j] == 0:
                    return [i, j]
            target += num
        