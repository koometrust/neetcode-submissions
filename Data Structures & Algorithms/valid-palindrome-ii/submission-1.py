class Solution:
    def validPalindrome(self, s: str) -> bool:

        # left, right = 0, len(s) - 1
        # count = 0

        # while left < right:
        #     # checking for inequality
        #     if s[left] != s[right]:
        #         count += 1
        #     #moving to the next elemnts
        #     left += 1
        #     right -= 1
        
        # if count == 1:
        #     return True 
        # return False

        left, right = 0, len(s) - 1

        while left < right:
            # checking for inequality
            if s[left] != s[right]:

                skipLeft, skipRight = s[left + 1:right + 1], s[left:right]
                #do palindrome check
                return skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1]
                #     return True
                # return False
            #moving to the next elemnts
            left += 1
            right -= 1
        
        return True
        


        