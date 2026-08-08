# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # floyds hare and tortoise
        # hare x2
        # tor 

        slow, fast = head, head  

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: #really cool btw
                return True
             

        return False
        
        return head.next






































        # slow, fast = head, head

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if fast == slow:
        #         return True
        # what would happen if we had a return false after return true
        # return False