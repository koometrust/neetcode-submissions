class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Input: s = "XYYX", k = 2

            # Output: 4
            if not s:
                return 0

            longestSub = 0

            l = 0
            counter = {}

            for r in range(len(s)):
                # counter[l] = 1 + counter.get(l, 0)
                counter[s[r]] = 1 + counter.get(s[r], 0)
                # slideLen = (r-l+1)


                # if len 0f sub - most common value freq > k = reduce window

                # if (r-l+1) - max(counter.values()) <= k:
                #     # r+=1
                #     longestSub = max(longestSub, r-l+1)
                # else:
                #     counter[s[l]] -= 1
                #     l+=1
                while (r-l+1) - max(counter.values()) > k:
                    counter[s[l]] -= 1
                    l+=1
                longestSub = max(longestSub, r-l+1)
                


            
            return longestSub



            # for each we record the longest substring length using max


            # else if len 0f sub - most common value freq < k = increse window.

























        # counter = {}
        # l = 0
        # lSeq = 0

        # # for r in range(l, len(s)):
        # for r in range(len(s)):

        #     counter[s[r]] = 1 + counter.get(s[r] , 0)
        #     # counter[r] = counter.get(r , 0)

        #     #while invalid: shrink
        #     while (r-l + 1) - max(counter.values()) > k:
        #         counter[s[l]] -= 1
        #         l+=1
        #     lSeq = max(lSeq, r-l+1)


        # return lSeq



        