class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # target = 10

        # for list in matrix:
        #     for l in list:
        #         if l == target:
        #             return True
        # return False

        #does not take advantage of it's sorted nature

        #binary search
        #implement Binary search on a sorted matrix

        # [ [1,2,4,8], [10,11,12,13] , [14,20,30,40] ]
        for list in matrix:
                    
                    l,r = 0, len(list) - 1

                    while l <= r:


                        m = (l + r) // 2
                        #check base case
                        if list[m] == target:
                            return True              
                        
                        
                        if list[m] > target:
                            r = m - 1
                        # elif list[m]  < target:
                        #     l  = m + 1
                        # else:
                        #     return True

                        else:
                            l  = m + 1
                        
                    
                            
        return False


                    






















































