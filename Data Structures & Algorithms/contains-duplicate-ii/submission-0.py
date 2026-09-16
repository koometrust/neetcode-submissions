# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         """
#         3

#         equal and then abs(i-j) <= k:
#            True
#         Fale

#             o(n)2

#         dups = 2,1,3,4,5,2
#                     return index & the value
#                     if value in dups:
#                         return index o(n)

#                         minus them <= k:
#                            return True
#                         False
#         false

#         [2,1,3,4,5,2] k = 1
#                       . . 
                      
#         how to minus the values in a list 
#         [1,7]  <=k
#           return True

#          """
#         # # Dup counter
#         # count = {}
#         # for i in nums:
#         #     count[i] = 1 + count.get(i, 0)
        

#         # #here we get the dup value
#         # for key,frequency in count.items():
#         #     if frequency == 2:
#         #         theDuplicate = key
    
#         # count = 0
#         # indexList = []
#         # for idx, value in enumerate(nums):
#         #     if value == theDuplicate and count <= 2:
#         #         indexList.append(idx)
#         #         count += 1

#         # #A list with the 2 indexes 
#         # # [ i, j]

#         # l, r = 0 , 1
#         # while l < r:
#         #     minus = indexList[l] - indexList[r]
#         #     if minus <= k:
#         #         return True
#         #     return False



#         # #if there is no duplicate in count.values return False


#         set = ()
#         l,r = 0, 0

#         while r < len(nums):
#             if 

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for L in range(len(nums)):
            for R in range(L + 1, min(len(nums), L + k + 1)):
                if nums[L] == nums[R]:
                    return True
        return False


        
        
            



        