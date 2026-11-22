from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        dist1 = Counter(s1)
        dist2 = Counter(s2[:len(s1)])
        l, r = 0, len(s1) - 1
        while r != len(s2) - 1:
            # print(f"dist 1 is {dist1}")
            # print(f"dist 2 is {dist2}")
            if dist1 == dist2:
                return True
            r += 1
            dist2[s2[r]] += 1
            dist2[s2[l]] -= 1
            l += 1
        return dist1 == dist2