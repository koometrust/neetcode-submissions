class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for i in s:
            if i.isalnum():
                new = i.lower()
                newStr += new
        return newStr == newStr[::-1]
       
    


       
        