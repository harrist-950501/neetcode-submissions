class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        rotation = 0
        while l <= r:
            m = l + (r - l) // 2
            if nums[(m - 1) % n] > nums[m]:
                rotation = m
                break
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1       

        l, r = 0, n - 1
        while l <= r:
            
            m = l + (r - l) // 2
            real = (m + rotation) % n
            if nums[real] == target:
                return real
            elif nums[real] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1
        