class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #  nums = [1,2,3,4,4]
        #                |   |
        # [2,10,30,35,35,35]
        #        |        |

        # first, dupFinder = 0, 1
        # while dupFinder <= len(nums) - 1:
        #     if nums[first] != nums[dupFinder]:
        #         dupFinder += 1
        #         first +=1
        #     if nums[first] == nums[dupFinder]: 
        #         dupFinder += 1
        #     else:
        #         nums1[first + 1] = nums[dupFinder]

        #     #change nums1[first + 1] = nums[dupFinder]

        # [2,10,30,35,35,35]
        #     f 
        #       d

        # while dupFinder <= len(nums)-1:
        #     if nums[first] == nums[dupFinder]:
        #         dupFinder += 1
        #     elif nums[first] != nums[dupFinder]:
        #         nums[first] = nums[dupFinder]
        #         first += 1
        #         dupFinder += 1

        # return first

        # \
        # \
        # \
        # \\CORRECT ONE
        # \
        # \


        # first, dupFinder = 1, 1

        # while dupFinder <= len(nums)-1:
        #     if nums[dupFinder] != nums[dupFinder - 1]:
        #         nums[first] = nums[dupFinder]
        #         first += 1            
        #     dupFinder += 1

        # return first

        # \
        # \
        # \
        # \

        numSet = set(nums)

        k = len(numSet)

        nums[:] = sorted(numSet)


        return k



            






            






       