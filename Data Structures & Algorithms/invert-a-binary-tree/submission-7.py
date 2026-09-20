# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if  not root:
        #     return None
        # # store = root.left
        # root.left, root.right = root.right, root.left
        # # root.left = root.right
        # # root.right = root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)
           

        # return root

        if not root:
            return None
        
        # # root.left, root.right = root.right, root.left
        # store = root.left
        # root.left = root.right
        # root.right = store

        # self.invertTree(root.left)
        # self.invertTree(root.right)
        #recursive approach

        # return root
        # stack = [root]

        # while stack:
        #     node = stack.pop()
        #     # node.left, node.right = node.right, node.left
        #     store = node.left
        #     node.left = node.right
        #     node.right = store

        #     if node.left: 
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)

        # return root


        # \\
        # \
        # \
        # \
        # \\
        # \
        if not root:
            return None
        
        from collections import deque
        # stack = [root]
        que = deque([root])

        while que:
            node = que.popleft()
            #node swap
            node.left, node.right = node.right, node.left

            if node.right:
                que.appendleft(node.right)
            if node.left:
                que.appendleft(node.left)

            
        return root






    


        