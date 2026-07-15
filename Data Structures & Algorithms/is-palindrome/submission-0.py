class Solution:
    def isPalindrome(self, s: str) -> bool:
        singlestr = ""
        for i in s:
            if i.isalnum():
                singlestr += i.lower()
        return singlestr == singlestr[::-1]

        