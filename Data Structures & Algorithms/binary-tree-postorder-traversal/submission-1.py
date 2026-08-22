# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #     return []
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

        if not root:
            return []
        from collections import deque
        results = deque()
        stack = [root]

        while stack:
            node = stack.pop()
            results.appendleft(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
        
        return list(results)


        