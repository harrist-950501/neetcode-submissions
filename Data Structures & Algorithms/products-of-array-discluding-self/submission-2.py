class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        left = 1
        for i, num in enumerate(nums):
            output[i] *= left
            left *= num

        right = 1
        for i in reversed(range(len(nums))):
            output[i] *= right
            right *= nums[i]

        return output