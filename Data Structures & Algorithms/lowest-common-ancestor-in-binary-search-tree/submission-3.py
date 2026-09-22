# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p:TreeNode ,  q:TreeNode) -> TreeNode:

        if not root: 
            return None
        #we ha

        currentNode = root

        while currentNode:

            if p.val < currentNode.val and q.val < currentNode.val:
            # Continue on left tree
                # return (self.lowestCommonAncestor(currentNode.left, p , q))
                currentNode = currentNode.left

            elif p.val > currentNode.val and q.val > currentNode.val:
            # continue on right tree
                # return (self.lowestCommonAncestor(currentNode.right, p, q))
                currentNode = currentNode.right


            # if p.val or q.val == currentNode.val:
            # #return the node(because it is the split)
            # #maybe currentNode is p or q
            # #return currentNode.val
            #     return currentNode
            else:
                return currentNode
            

            # Time o(log n)
            #space O(1) Constant Time


             

