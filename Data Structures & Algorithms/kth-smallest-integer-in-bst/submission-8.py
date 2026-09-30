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
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # if not root:
        #     return 0
        # stack = [root]
        # nodesArray = []

        # while stack:
        #     node = stack.pop()
        #     nodesArray.append(node.val)

        #     if node.left:
        #         stack.append(node.left)

        #     if node.right:
        #         stack.append(node.right)

        # nodesArray.sort() #log n

        # return nodesArray[k-1]



        nodesArray = []

        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            nodesArray.append(node.val)
            dfs(node.right)


        dfs(root)
        return nodesArray[k - 1]

        # arr = []

        # def dfs(node):
        #     if not node:
        #         return
        #     dfs(node.left)       # everything smaller
        #     arr.append(node.val) # this node
        #     dfs(node.right)      # everything larger

        # dfs(root)
        # return arr[k - 1]



        


#         # edge cases
#         if not root:
#             return 0

#          global counter = 1
#         currentNode = root

#         if counter != k:
#             counter += 1
#             return (self.kthSmallest(currentNode.left, k))
#         return currentNode.val

# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         arr = []

#         def dfs(node):
#             if not node:
#                 return

#             dfs(node.left)
#             arr.append(node.val)
#             dfs(node.right)

#         dfs(root)
#         return arr[k - 1]

# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:



        # arr = []

        # def dfs(node):
        #     if not node:
        #         return

        #     arr.append(node.val)
        #     dfs(node.left)
        #     dfs(node.right)

        # dfs(root)
        # arr.sort()
        # return arr[k - 1]
     
        


 

    # iterate through the tree and store the node values in a sorted array 
    # o(n log n) time
    # o(n)space
    # return arr[k+1]

    # optimizations
    #use BST nature to our advantage.

    # o(n) time
    # constant space o(1)
    #maybe a traversal technique that is relevant (inorder)
    # return the kth step during the traversal

    





        





    




        