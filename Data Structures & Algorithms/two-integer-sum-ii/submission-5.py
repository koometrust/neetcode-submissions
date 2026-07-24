class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else: #if we are not greater than or less than target then we are target
                return [l + 1, r + 1]
        return []

            #numbers[l] the actual number
            # l the index of the number
          

