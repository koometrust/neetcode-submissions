class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """


        # list3 = []
        # i, j = 0, 0

        # while i < m and j < n:

        #     if nums1[i] < nums2[j]:
        #         list3.append(nums1[i])
        #         i += 1
        #     else: 
        #         list3.append(nums2[j])
        #         j += 1
        
        # list3.extend(nums1[i:m])
        # list3.extend(nums2[j:])

        # nums1[:] = list3
    


        # return list3
        # /
        # /
        # /
        # /
        # /

        # in nums1 we have 2 pointers

        last, pointer1 = len(nums1) - 1, m - 1

        #in nums2 we have 1 pointer
        pointer2 = len(nums2) - 1 #i think we can also use n

        while pointer1 >= 0 and pointer2 >= 0:
            if nums2[pointer2] > nums1[pointer1]:
                nums1[last] = nums2[pointer2]
                pointer2 -=1
            else: 
                nums1[last] = nums1[pointer1]
                pointer1 -= 1
            last -=1

        while pointer2 >= 0:
            nums1[last] = nums2[pointer2]
            pointer2 -= 1
            last -= 1
        

        # last = m + n - 1

        # # Merge in reverse order
        # while m > 0 and n > 0:
        #     if nums1[m - 1] > nums2[n - 1]:
        #         nums1[last] = nums1[m - 1]
        #         m -= 1
        #     else:
        #         nums1[last] = nums2[n - 1]
        #         n -= 1
        #     last -= 1

        # # Fill nums1 with leftover nums2 elements
        # while n > 0:
        #     nums1[last] = nums2[n - 1]
        #     n -= 1
        #     last -= 1



            

















     




        


        