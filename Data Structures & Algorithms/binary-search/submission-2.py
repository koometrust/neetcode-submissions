class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # trivial solution/
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1


        #take advantage of it's sorted nature
        # [-1,0,2,4,6,8]
        #  l    m     r

        l,r = 0, len(nums) - 1

        while l <= r: 
            m = (l + r) // 2
            #check base case
            if nums[m] == target:
                return m

             # [-1,0,2,4,6,8]
             #  l    m     r
        
            if nums[m] > target:
                r = m-1
            else:
                l = m + 1
            
        return -1
 

#there are other different forms of Binary search

        