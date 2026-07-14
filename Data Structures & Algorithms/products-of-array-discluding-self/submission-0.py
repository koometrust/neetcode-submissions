class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Input: nums = [1,2,4,6]
        # Output: [48,24,12,8]   
        res = [1] * len(nums)
        prefix = 1
        for num in range(len(nums)):
            res[num] = prefix #that's how I'll go changing the number along the way
            prefix *= nums[num]
        postfix = 1
        for num in range(len(nums) -1 ,-1, -1):
            res[num] *= postfix
            postfix *= nums[num]
        return res

    
            



