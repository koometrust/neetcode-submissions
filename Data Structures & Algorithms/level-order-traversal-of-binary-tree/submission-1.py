# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #this is BFS
        #sijaona kama inaeza fanywa recursively

        if not root:
            return []
        from collections import deque
        res = []
        que = deque([root])

        while que:
            r_row = []
            for _ in range(len(que)):
                node = que.popleft()
                r_row.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            res.append(r_row)
        return res
            
                    


        