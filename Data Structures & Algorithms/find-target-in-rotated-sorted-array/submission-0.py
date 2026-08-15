class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #sorted we have the advantage of Binary search
        # l m r
        #middle is the attempt to find the pivot
        #the separator of the subarraays
        #return index if present else -1

        #[3,5,6,0,1,2]
        # l     m   r
        #know which subarray m is in
        #check base case first is M == target
        # two left, two right

        l, r = 0, len(nums) -1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            

            if nums[m] >= nums[l]: #whats the equals for
                    #m is in left side
                    #if > l or if > r:
                    # m-1
                    # if target > nums[l] or target > nums[r]:
                    #     l = m -= 1
                    # else: 
                    #     m+1
                if target < nums[l] or target > nums[m]:
                    # l = m += 1 why + 1 and not += 1
                    l = m + 1
                else: 
                    r = m - 1
            else:
                #m is on right side
                #if < r or if < l
                # m+1
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
                
        return -1



                        
# why do I occasionall get this error: Time Limit Exceeded. You may have an infinite loop or your code is too inefficient.







