class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            num = nums[i]
            if num > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            right = len(nums) - 1
            left = i + 1
            while right > left:
                leftNum = nums[left]
                rightNum = nums[right]
                numSum = num + leftNum + rightNum
                if numSum == 0:
                    output.append([num, leftNum, rightNum])
                    left += 1
                    right -= 1
                    while right > left and nums[left] == nums[left - 1]:
                        left += 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
                elif numSum > 0:
                    right -= 1
                else:
                    left +=1
        return output


        