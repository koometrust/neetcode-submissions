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
        # from collections import deque
        # que = deque(nums)

        # n = len(nums)
        # k %= n

        # # while k > 0:
        # #     popped = que.pop()
        # #     que.appendleft(popped)
        # #     k -= 1

        # que.rotate(k)

        # nums[:] = list(que)

        
        # \
        # \
        # \
        # \
        """

        nums = [1,2,3,4,5], k = 2

        output = [4,5,1,2,3]

               reverse 3 times

               -[5,4,3,2,1]

               [5,4,1,2,3]

        nums= [4,5,1,2,3]

               
               
        """

        # nums.reverse() # 5,4,3,2,1

        # reverseSecondPart = (len(nums) - k) - 1
        # nums.reverse(nums[reverseSecondPart:]) #[5,4,1,2,3]

        # firstPart = k-1
        # nums.reverse(nums[:firstPart]) #[4,5,1,2,3]
        k = k % len(nums)

        l,r = 0, len(nums) - 1

        while l < r:
            #do it in one line so we dont need storage
            nums[l],nums[r] = nums[r], nums[l]

            l+=1
            r-=1


        l,r = 0, k-1

        while l < r:
            #do it in one line so we dont need storage
            nums[l],nums[r] = nums[r], nums[l]
            
            l+=1
            r-=1


        l,r = k, len(nums) - 1

        while l < r:
            #do it in one line so we dont need storage
            nums[l],nums[r] = nums[r], nums[l]
            
            l+=1
            r-=1












        

        


        