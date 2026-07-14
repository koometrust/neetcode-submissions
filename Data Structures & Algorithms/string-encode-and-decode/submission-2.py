class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))     
            res.append('#')
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # ->yayy 3#for2#s# ->
        i = 0        #i ji
        decoded = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) #1 j = 2
            i = j + 1 # 2 + 1=3
            j = i + length 
            decoded.append(s[i:j]) #for
            i = j

        return decoded


        