# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         # s = "OUZODYXAZV", t = "XYZ"
#         # Output: "YXAZ"

#         #need t
#         #what we currently have in the window and does it satisfy what we need
#         if s == '': return ''

#         need = {}
#         for i in s:
#             need[i] = 1 + need.get(i, 0) 

#         window = {}
#         l,r = 0, 0

#         needInt = len(need)
#         want = 0
#         res, resLen = [-1, -1], float("infinity")


#         while r <= len(s):
#             # if s[r] in need:
#             #     window[s[r]] = 1 + window.get(s[r], 0)
#             #     if needInt == want:
#             #         l + 1

#             #     elif needInt > want: 
#             #         want += 1
#             #         r 
#             c = s[r]
#             window[c] = 1 + window.get(c, 0)

#             if c in need and window[c] == need[c]:
#                 want +=1 

#             while needInt == want:
#                 if(r-l +1) < resLen:
#                     res = [l,r]
#                     resLen = r-l + 1
#                 window[s[l]] -= 1
#                 if s[l] in need and window[s[l]] < countT[s[l]]:
#                     want -= 1
#                 l += 1
#         l, r = res
#         return s[l : r + 1] if resLen != float("infinity") else ""



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""




        