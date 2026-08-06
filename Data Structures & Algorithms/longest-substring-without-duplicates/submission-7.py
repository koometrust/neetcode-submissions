class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        l = 0
        hashS = set()

        for r in range(l, len(s)):
            # if s[r] in hashS:
            while s[r] in hashS:
                 # sliding window use while to move the L
                hashS.remove(s[l])
                l+=1
            hashS.add(s[r])
            # count = max(count, len(hashS))
            count = max(count, r - l + 1)
        return count

        


























































        
        # store = []
        # count = 0
        # for i in s:
        #     if ord(i) - 1 in s:
        #         continue
        #     l ,r = i, i+1

        #     while l < r:


        #         if ord(r) not in 
        res = 0

















                          
        # for i in range(len(s)):
        #     charSet = set()
        #     for j in range(i, len(s)):
        #         if s[j] in charSet:
        #             break
        #         charSet.add(s[j])
        #     res = max(res, len(charSet))
        # return res

                





            #longest sequence of continous characters
        