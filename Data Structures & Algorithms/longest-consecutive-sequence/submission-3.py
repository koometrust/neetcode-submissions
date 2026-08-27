class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)
        lSequence = 0

        #loop through cheching if element -1 exists
        # ...
        #we have a counter and we now look for Element + 1

        for i in numSet:
            if i - 1 in numSet:
                continue

            length = 1
            while i + length in numSet:
                length += 1
            lSequence = max(lSequence, length)
        
        return lSequence


        #   for i in range(len(numSet)):
        #     if numSet[i] - 1 in numSet:
        #         continue

        #     length = 1
        #     while numSet[i] + length in numSet:
        #         length += 1
        #     lSequence = max(lSequence, length)
        
        # return lSequence
            
            
            



            # while numSet[i] + 1 in numSet:
            #     counter += 1
            #     numSet[i] += 1
            # lSequence = max(lSequence, counter)





















#         numSetSet = set(numSet)
#         longest = 0

# #my personal attempt which passed the first two tests but threw an error of:
# # Traceback (most recent call last):
# #   File "/box/main.py", line 43, in main
# #     output = solution.longestConsecutive(input)
# #   File "/box/main.py", line 18, in longestConsecutive
# #     while num + count in numSetSet:
# #                 ^^^^^
# # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value


#         for num in numSetSet:
#             if num - 1 not in numSetSet:
#                 count = 1
#                 while num + count in numSetSet:
#                     count +=1
#                     if count >= longest:
#                         longest = count
#         return longest

#         #The Correct answer.

#             # for num in numSetSet:
#             #     if (num - 1) not in numSetSet:
#             #         length = 1
#             #         while (num + length) in numSetSet:
#             #             length += 1
#             #         longest = max(length, longest)
#             # return longest



                