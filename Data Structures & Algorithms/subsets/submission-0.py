class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        path = []

        def dfs(i):
            if i == len(nums):
                output.append(path.copy())
            else:
                dfs(i + 1)
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return output