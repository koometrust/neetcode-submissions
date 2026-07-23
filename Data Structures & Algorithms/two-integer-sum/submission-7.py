class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        complement = 0
        for idx, num in enumerate(nums):

            complement = target - num
            if complement in seen: #only checks keys
                return [seen[complement], idx]
            seen[num] = idx #storing part
            #what we're looking for is what we store as the key. thats why we store seen[num]



   