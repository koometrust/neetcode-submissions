# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

      # Input: head = [0,1,2,3]

      # Output: [3,2,1,0]

        # 1<-2<-3

      #  <-1 2->3->4
        #            c
  #                p
      prev, curr = None, head

      while curr:
        # curr.next = store
        store = curr.next #storage
        curr.next = prev
        prev = curr
        curr = store


      return prev

        



























      # #0 -> 0
      # #    0 <- 0 -> 0 <-0  ...none
      # # store the next pointer
      # # we flip
      # # we move

      # prev, curr = None, head

      # while curr:
      #   store = curr.next
      #   curr.next = prev
      #   prev = curr
      #   curr = store
      # return prev





















        



      # prev, curr = None, head

        # while curr: \/
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # return prev