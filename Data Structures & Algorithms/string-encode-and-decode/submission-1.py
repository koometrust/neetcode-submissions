class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
    
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#': # what if I said  if j is not "#":is this correct syntax
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length #explain this line cause I don't see why we need to add length cant we just say I is = j right here and restart the loop 
            res.append(s[i:j]) #I assume this appends from i to J on the res array but isn't i == the number at the begining or it only starts counting after the hash so s[i:j] means after and before the the hashes. please explain
            i = j

        return res

