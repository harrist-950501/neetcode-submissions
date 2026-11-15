class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s))
            output += "/"
            output += s
        print("Encode as: " + output)
        return output
    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            countS = ""
            while s[i] != "/":
                countS += s[i]
                i += 1
            i += 1
            print(countS)
            count = int(countS)
            output.append(s[i: i + count])
            i += count
        return output