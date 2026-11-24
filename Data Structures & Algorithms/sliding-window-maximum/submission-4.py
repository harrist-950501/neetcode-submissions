from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        curMax = deque()
        output = []

        l = 0
        for r in range(len(nums)):
            while curMax and curMax[-1] < nums[r]:
                curMax.pop()
            curMax.append(nums[r])

            if r - l == k:
                if nums[l] == curMax[0]:
                    curMax.popleft()
                l += 1

            if r >= k - 1:
                output.append(curMax[0])

        return output