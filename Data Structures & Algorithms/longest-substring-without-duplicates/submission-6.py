class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSub = 0
        l = 0
        subSet = set()
        for r in range(len(s)):
            while s[r] in subSet:
                subSet.remove(s[l])
                l += 1
            subSet.add(s[r])
            longestSub = max(longestSub, r - l + 1)
        return longestSub