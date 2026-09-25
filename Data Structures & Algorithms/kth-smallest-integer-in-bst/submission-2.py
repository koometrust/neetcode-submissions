# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    """
    Pseudo rough work
        1234567
        [123456] -> 4 o(n)space, o(nlogn) 4th for _ in range(4)
        
        DFS on the Tree and return the curr.val == k:


         o root
        / \
     o.l   o.r



    # inOrder Traversal
    1234567
        [123456] -> 4
        counter = 1
        counter == k:
          return node.val
    """
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

#         # edge cases
#         if not root:
#             return 0

#          global counter = 1
#         currentNode = root

#         if counter != k:
#             counter += 1
#             return (self.kthSmallest(currentNode.left, k))
#         return currentNode.val

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        return arr[k - 1]
        





    




        