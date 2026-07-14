class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numsSet: #you can't start with an if bro (trap hapo)
                length = 0
                while (n + length) in numsSet:
                    length += 1
                longest = max(length, longest) #bado kuelewa

        return longest


                