class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        reversed = []
        while s:
            reversed.append(s.pop())

        s[:] = reversed
        
        return s
        