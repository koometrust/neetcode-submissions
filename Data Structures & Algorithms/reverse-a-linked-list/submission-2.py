# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        # 0-> 0
        # 0<- 0
        while curr:
          nxt = curr.next #hii ni nomaaaaa
          curr.next = prev
          prev = curr #we move prev forward or is this the pointer instead of the node
          curr = nxt #we move curr forward or is this the pointer instead of the node

        return prev



      # prev, curr = None, head

        # while curr: \/
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # return prev