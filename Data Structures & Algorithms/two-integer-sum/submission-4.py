class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_num = {} # empty hashmap
        
        for idx, num in enumerate(nums):
            key = num
            value = idx
            complement = target - num 
            if complement in seen_num:
                return [seen_num[complement], idx]
            seen_num[key] = value
                
        return twoSum
                






# num i + num j = target