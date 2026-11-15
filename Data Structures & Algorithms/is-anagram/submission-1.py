class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCount = {}
        tCount = {}

        for char in s:
            sCount[char] = 1 + sCount.get(char, 0)

        for char in t:
            tCount[char] = 1 + tCount.get(char, 0)

        return sCount == tCount

