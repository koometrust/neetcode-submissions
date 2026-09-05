class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """


        # s = ["n","e","e","t"]

        # ["t","e","e","n"]

        left, right = 0, len(s) - 1

        while left <= right:
            #switch the left and right values
            store = s[left]
            s[left] = s[right]
            s[right] = store
            #move the pointers inwards
            left += 1
            right -= 1
        
        return s

            









    
    
    # \
    # \
    # \
    # \
    # \
    # \

        
        # reversed = []
        # while s:
        #     reversed.append(s.pop())

        # s[:] = reversed
        
        # # return s