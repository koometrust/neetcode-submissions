class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        l = 0
        lSeq = 0

        # for r in range(l, len(s)):
        for r in range(len(s)):

            counter[s[r]] = 1 + counter.get(s[r] , 0)
            # counter[r] = counter.get(r , 0)

            #while invalid: shrink
            while (r-l + 1) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l+=1
            lSeq = max(lSeq, r-l+1)


        return lSeq



        