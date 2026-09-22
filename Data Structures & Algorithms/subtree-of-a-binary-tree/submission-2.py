# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #DFS till value that is same as subroor
        #I will I can do recursion with the SameTree() as helper function also as boilerplate:
        #   return either true or false

        #iteratively
        #iterstive same tree comparison but I only start the comparison when node of root == node of subroot


        # edge cases
        if not subRoot:
            return True

        if not root and subRoot: 
            return False

        # if not root and not subRoot: 
        #     return True

        # recursively go compare root the subroot
        if self.sameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))



    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode])-> bool:
        # edge cases
        # recursively go throught the tree
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False
        
        if root.val == subRoot.val:
            #explain this recursion and what it does
            return (self.sameTree(root.left, subRoot.left) and
                    self.sameTree(root.right, subRoot.right))

        
        return False


        """
        So isSubtree walks root looking for a starting point; sameTree walks both trees in lockstep once a candidate start is found.
        """

        








        