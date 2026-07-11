class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = set()
        for i in nums:
            if  i in dups:
             return True
            dups.add(i)
        return False
        
        
        
        
        
        
        
        
        
        
        #    .
    #    .
    #    ..
    #    .
    #    .
    #    .
    #    .
    #    .
    #    .
    #    ..
    #    .
    #    .
    #    .
    #    .
    #    .
    #    .
    #    .
    #    .
    #    .
    #    .
    #    .
    #    .
    #    .
    #     # nums=[1,2,3,3]
    #     seen = set()
    #     for num in nums:
    #      if num in seen:
    #         return True
    #      seen.add(num)
    #     return False
