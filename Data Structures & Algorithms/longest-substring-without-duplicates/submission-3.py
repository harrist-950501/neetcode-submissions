class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSub = 0
        f, e = 0, 0
        subSet = set()
        while e < len(s):
            if s[e] not in subSet:
                subSet.add(s[e])
                e += 1
            else:
                subSet.remove(s[f])
                f += 1
            longestSub = max(longestSub, e - f)
        return longestSub
        