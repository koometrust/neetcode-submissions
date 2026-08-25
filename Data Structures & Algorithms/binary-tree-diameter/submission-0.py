# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # if not root: 
        #     return 0
        
        # stack = [root]
        # largestd = 0
        # leftHeight ,rightHeight = 0,0


        # while stack:
        #     node = stack.pop()


        #     if node.right:
        #         stack.append(node.right)
        #         rightHeight += 1 
        #     if node.left:
        #         stack.append(node.left)
        #         leftHeight += 1 

        #     d = leftHeight + rightHeight
        #     largestd = max(largestd,d)

        # return largestd
        # /
        # /
        # //
        # /

        # /
        # /
        # /
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)


        dfs(root)
        return res
        




            

            
        