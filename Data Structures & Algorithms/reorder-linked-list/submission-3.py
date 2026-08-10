# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow , fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondl = slow.next #the start of the second ll
        prev = None
        slow.next = None #i dont know why
        while secondl:
            store = secondl.next #reuse
            secondl.next = prev
            prev = secondl
            secondl = store

        #merge the two LL there will be storing of pointers
        #define heads of both LL
        #and store they're pointers

        first, second = head, prev #can't use second cause it's None
        while second:
            store1, store2 = first.next , second.next
            first.next = second
            #second = store1 #but this one failed can't we say second node points to first.next which is store 1
            second.next = store1
            first = store1
            second = store2






       