class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # slow, fast, slow2  = 1, 1, 1
        # slow = nums[slow]
        # fast = nums[nums[fast]]

        # while len(nums) > slow: #nums
        #     slow += 1
        #     fast += 2

        #     if slow == fast:
        #         slow2 += 1
        #         if slow2 == slow:
        #             return slow2
        #         slow2 += 1
        #         slow += 1

            #p = x

        slow , fast = 0 , 0
        while nums:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
         
        slow2 = 0
        while nums:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            







        