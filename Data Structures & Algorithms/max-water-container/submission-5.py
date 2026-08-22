class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Input: height = [1,7,2,5,4,7,3,6]

        # Output: 36

        maxContainer = 0
        l,r = 0, len(heights)-1

        while l < r: 
            area = min(heights[l], heights[r]) * (r-l)
            if heights[l] < heights[r]:
                maxContainer = max(maxContainer, area)
                l+=1
            else:
                maxContainer = max(maxContainer, area)
                r-=1
        
        return maxContainer
                























    #    areas = []
    #    max = 0

    #    l, r = 0 , len(heights)-1
    #    while l < r:
    #     #    width = r - l
    #     #    length = min(heights[l], heights[r])
    #        area = (r-l) * min(heights[l], heights[r])
    #        if heights[l] > heights[r]:
    #            r -=1
    #        elif heights[l] < heights[r]:
    #            l+=1
    #        else:
    #            l+=1

    #        areas.append(area)
    #    areas.sort()
    #    max = areas.pop()




    #    return max
               