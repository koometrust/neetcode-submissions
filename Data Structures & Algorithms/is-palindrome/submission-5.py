class Solution:
    def isPalindrome(self, s: str) -> bool:
       testpal = ''
       for i in s:
        if i.isalnum():
            testpal += i.lower()
       return testpal == testpal[::-1]



       
        