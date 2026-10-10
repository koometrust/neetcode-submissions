class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      S = sorted(s)
      T = sorted(t)
      return S == T
      #   return True
      # return False 











      # s = sorted(list(s))
      # t = sorted(list(t))
      # return s==t
       

        