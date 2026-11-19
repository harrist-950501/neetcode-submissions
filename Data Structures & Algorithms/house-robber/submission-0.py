class Solution:
    def rob(self, nums: List[int]) -> int:
        money = [0] * (len(nums) + 2)

        for i in range(len(nums)):
            money[i + 2] = max(money[i] + nums[i], money[i + 1])

        return money[len(nums) + 1]