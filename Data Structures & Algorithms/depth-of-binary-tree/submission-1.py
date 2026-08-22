# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # maxDepth , count = 0, 1
        # res = []
        # stack = [root]

        # while stack:
        #     node = stack.pop()
        #     # res.append(node.val)
        #     # count += 1
        #     # maxDepth = max(maxDepth, count)
            

        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         count +=1
        #         maxDepth = max(maxDepth, count)
        #         stack.append(node.left)

        # return maxDepth
 
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right) )
        # return depth


        