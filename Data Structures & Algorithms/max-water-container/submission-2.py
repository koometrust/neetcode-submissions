class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # res = []
        # maji = []

        # for i,val in enumerate(heights):

        #     l,r = i, len(heights) - 1

        #     while l < r:
        #         dis = r - l
        #         if heights[l] > heights[r]:
        #             sum = heights[r] * dis
        #             maji.append(sum)
        #             r-=1
        #         elif heights[l] < heights[r]:
        #             sum = heights[l] * dis
        #             maji.append(sum)
        #             l+=1
        #         else: 
        #             sum = heights[l] * dis
        #             maji.append(sum)
        #             l+=1
        #             r-=1

        #     maji.sort()
        #     res.append(maji.pop())

        # return int(res)
        res = 0


        l,r = 0, len(heights) - 1

        while l < r:
            dis = r - l
            area = min(heights[r], heights[l]) * dis
            res = max(res, area)

            if heights[l] > heights[r]:
                r-=1
            # elif heights[l] < heights[r]:
            #     l+=1
            else: 
                l+=1

        

        return res





        