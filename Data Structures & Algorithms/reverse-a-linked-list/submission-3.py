# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

      #0 -> 0
      #    0 <- 0 -> 0 <-0  ...none
      # store the next pointer
      # we flip
      # we move

      prev, curr = None, head

      while curr:
        store = curr.next
        curr.next = prev
        prev = curr
        curr = store
      return prev





















        



      # prev, curr = None, head

        # while curr: \/
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # return prev