class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # [ [1,2,4,8], [10,11,12,13] , [14,20,30,40] ]
        # target = 10

        for list in matrix:
            for l in list:
                if l == target:
                    return True
        return False

