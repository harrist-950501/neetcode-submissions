from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramToStr = {}
        for s in strs:
            lowerLetterCount = [0] * 26
            for c in s:
               lowerLetterCount[ord(c) - ord('a')] += 1
            anagram = tuple(lowerLetterCount)
            if anagram in anagramToStr:
                anagramToStr[anagram].append(s)
            else:
                anagramToStr[anagram] = [s]

        output = [];
        for anagram in anagramToStr:
            output.append(anagramToStr[anagram])
        return output