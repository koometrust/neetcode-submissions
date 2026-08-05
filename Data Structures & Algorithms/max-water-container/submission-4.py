class Solution:
    def maxArea(self, heights: List[int]) -> int:
       areas = []
       max = 0

       l, r = 0 , len(heights)-1
       while l < r:
        #    width = r - l
        #    length = min(heights[l], heights[r])
           area = (r-l) * min(heights[l], heights[r])
           if heights[l] > heights[r]:
               r -=1
           elif heights[l] < heights[r]:
               l+=1
           else:
               l+=1

           areas.append(area)
       areas.sort()
       max = areas.pop()




       return max
               