"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        from collections import deque
        results = deque()
        stack = [root]

        while stack:
            node = stack.pop()
            results.appendleft(node.val)

            for child in node.children:
                stack.append(child)

            # if node.left:
            #     stack.append(node.left)
            # if node.right:
            #     stack.append(node.right)
            
        
        return list(results)
        