from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        sl, sr = 0, float('infinity')
        tCount = Counter(t)
        sCount = Counter()
        need = len(tCount)
        have = 0
        l = 0
        for r in range(len(s)):
            sCount[s[r]] += 1
            if sCount[s[r]] == tCount[s[r]]:
                have += 1
            while need == have:
                if sr - sl > r - l:
                    sl, sr = l, r
                sCount[s[l]] -= 1
                if sCount[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1

        if sr == float('infinity'):
            return ""
        return s[sl: sr + 1]
        