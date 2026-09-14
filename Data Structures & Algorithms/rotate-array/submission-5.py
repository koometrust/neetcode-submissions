class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        nums = [1,2,3,4,5,6,7,8], k = 2

               [5,6,7,8,1,2,3,4]

               t = o(k)
               s = constant
               pop k times -> appendleft k times on array nums
        """
        from collections import deque
        que = deque(nums)

        n = len(nums)
        k %= n

        # while k > 0:
        #     popped = que.pop()
        #     que.appendleft(popped)
        #     k -= 1

        que.rotate(k)

        nums[:] = list(que)
        


        