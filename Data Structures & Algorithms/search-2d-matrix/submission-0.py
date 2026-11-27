class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cLen, rLen = len(matrix), len(matrix[0])
        l, r = 0, rLen * cLen - 1
        while l < r:
            m = l + (r - l) // 2
            mr, mc = m // rLen, m % rLen
            mVal = matrix[mr][mc]
            if mVal == target:
                return True
            elif mVal > target:
                r = m - 1
            else: 
                l = m + 1
        
        return matrix[r // rLen][r % rLen] == target
        