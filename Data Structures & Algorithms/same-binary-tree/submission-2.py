# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #check base case(if null) use and
        #choose a traversal technique
        #iterate through both trees return false if nodes != 

        if not p and not q:
            return True

        if not p or not q: 
            return False
        
        #lets use DFS
        stackP, stackQ = [p], [q]
        
        while stackP and stackQ:

            nodeP, nodeQ = stackP.pop(), stackQ.pop()

            if nodeP is None and nodeQ is None:
                continue
            if not nodeP or not nodeQ:
                return False
    
            #compare the nodes
            if nodeP.val != nodeQ.val:
                return False

            #Do the normal Travesal DFS
            # if nodeP.left and nodeQ.left:
            stackP.append(nodeP.left)
            stackQ.append(nodeQ.left)
            # if nodeP.right and nodeQ.right:
            stackP.append(nodeP.right)
            stackQ.append(nodeQ.right)


        return True

        #recursion
        #inatumia self
        # if not p and not q:
        #     return None

        # return (self.preOrder(p.left and q.left), self.preOrder(p.val and q.val), self.preOrder(p.right and q.right)

        # if self.isSameTree(p.left != q.left or p.right != q.right or p.val != q.val:





        