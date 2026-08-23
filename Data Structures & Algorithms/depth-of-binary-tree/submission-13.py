# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        que = deque([root])
        depth = 0

        while que:


            for i in range(len(que)):

                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            depth +=1
        
        return depth
            






















    #     if not root:
    #         return 0

    #     stack = [[root, 1]]
    #     res = 1
    #     while stack:
    #         node, depth = stack.pop()
            
    #         if node: 
    #             res =  max(res,depth)
    #             stack.append([node.left, depth + 1])
    #             stack.append([node.right, depth + 1])
                
    #     return res


        # \
        # \
        # \
        # \
        # \

        # if not root:
        #     return 0

        # from collections import deque
        # level = 0
        # que = deque([root])

        # while que:
        #     # [1,2,3,null,null,4]
            
        #     for i in range(len(que)):
        #         node = que.popleft()
        #         if node.left:
        #             que.append(node.left)
        #         if node.right:
        #             que.append(node.right)
        #     level +=1
                
        # return level
        
    # \
    # \
    # \
    # \
    # \
    # \

        # if not root:
        #     return 0
        # maxDepth , count = 0, 1
        # res = []
        # stack = [root]

        # while stack:
        #     node = stack.pop()
        #     # count += 1
        #     # maxDepth = max(maxDepth, count)
            

        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        # count +=1
        # # maxDepth = max(maxDepth, count)

        # return count


# \
# \
# \
# \
# \
# \
# \
# \
# \
# \
# \

        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right) )
        # # return depth


        