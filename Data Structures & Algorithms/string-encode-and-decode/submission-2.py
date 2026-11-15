class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += ".".join([str(ord(c)) for c in s])
            output += "/"
        return output
            

    def decode(self, s: str) -> List[str]:
        print("str is " + s)
        output = []
        for ordS in s.split("/")[:-1]:
            print("ordS is " + ordS)
            string = "";
            if not ordS == "":
                for ordC in ordS.split("."):
                    print("ordC is " + ordC)
                    string += chr(int(ordC));
            output.append(string)
        return output