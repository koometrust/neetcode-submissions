class Solution:
    def findMin(self, nums: List[int]) -> int:
        l ,r = 0 , len(nums) - 1

        # nums = [3,4,5,6,1,2] 12345 45123
                # l     m l  r
        small = nums[0]

        while l <= r:
            m = (l + r)// 2 
            if nums[l] < nums[r]:
                small = min(small ,nums[l])
                break
            small = min(small ,nums[m]) #why here why m

            if nums[m] >= nums[l]:
                #search right
                l = m + 1
            else:
                #search left
                r = m-1
            
            
        return small

        