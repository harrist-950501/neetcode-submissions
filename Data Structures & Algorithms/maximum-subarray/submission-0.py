class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mSumSub = float('-inf') # max sum of subarray
        bSumSub = float('-inf') # best sum of sub so far
        for num in nums:
            if num >= num + bSumSub:
                bSumSub = num
            else:
                bSumSub += num
            mSumSub = max(mSumSub, bSumSub)

        return mSumSub
        