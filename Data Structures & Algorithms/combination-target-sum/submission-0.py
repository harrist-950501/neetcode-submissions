class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        com = []

        def explore(i, curT):
            if curT == 0:
                output.append(com.copy())
            elif i < len(nums) and curT > 0:
                com.append(nums[i])
                explore(i, curT - nums[i])
                com.pop()
                explore(i + 1, curT)

        explore(0, target)
        return output



        