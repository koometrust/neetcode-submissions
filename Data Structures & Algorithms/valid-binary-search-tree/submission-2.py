# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         #if statement to check if left subtree is smaller than root node
#         #if statement to check if right subtree nodes is > than root node

#         # currentNode = root

#         # if currentNode.left > currentNode:
#         #     return False
#         # elif currentNode.right < currentNode:
#         #     return False
#         # else: 
#         #     return True

#         #     #               o
#         #     #         o.l       o.r
#         #     # # lesser            greater

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))
        



        