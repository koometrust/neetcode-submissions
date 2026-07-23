class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        complement = 0
        for idx, num in enumerate(nums):
            key = idx
            value = num

            complement = target - num
            if complement in seen: #only checks keys
                return [seen[complement], key]
            seen[value] = key #storing part

            # seen[key] = complement #storing part


   