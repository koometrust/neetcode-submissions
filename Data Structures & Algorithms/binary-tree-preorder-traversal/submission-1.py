# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                #LIFO lAST INTO THE STACK FIRST OUT
        
        return result


        # if not root:
        #     return []
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        # Input: root = [1,2,3,4,5,6,]

        # Output: [1,2,4,5,3,6,7]



            


        