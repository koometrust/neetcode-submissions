class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """


        list3 = []
        i, j = 0, 0

        while i < m and j < n:

            if nums1[i] < nums2[j]:
                list3.append(nums1[i])
                i += 1
            else: 
                list3.append(nums2[j])
                j += 1
        
        list3.extend(nums1[i:m])
        list3.extend(nums2[j:])

        nums1[:] = list3
    


        # return list3





     




        


        