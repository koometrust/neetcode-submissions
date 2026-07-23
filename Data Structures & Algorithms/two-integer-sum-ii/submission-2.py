class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # # for idx,num in enumerate(numbers):
        #     othernum = target - num
        #     if othernum in numbers:
        #         return [num, othernum]
            
    

    #   for num in mums:
    #         othernum = target - num
    #         if othernum in nums and != num:
    #             return [num,othernum]

        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target and numbers[i] != numbers[j]:
                    return [i+1, j+1]


