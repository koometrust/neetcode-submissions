# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#reorder list my favourite question.

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # # Input: head = [2,4,8,6]

        # # Output: [2,8,4,6]

        # fast, slow = head, head

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if fast:
        #         startL2 = slow #centre node
        #         #reverse everything after here
        #         # prev and curr nodes

        # #we need to have none and head
        # startL2 = None
        # frontStartL = startL2

        # #reversing
        #     # <-2 4->6->8
        # #         c
        # #       p

        # # while startL2:

        # #     store = startL2.next
        # #     startL2.next = startL2
        # #     startL2 = startL2.next
        # #     startL2.next = store

        # # [0 ->1-> 2->3<-6 <-5<-4]
        # # [0  6, 1, 5-> 2, 4, 3]
        # #              ->
        # #   <-
        
        # l1, l2 = head, frontStartL
        # while l1:
        #     store1, store2 = l1.next, l2.next
        #     l1.next = l2
        #     l2.next = store1
        #     l1 = store1
        #     l2 = store2
        
        # return l1


        # if not head:
        #     return

        # arr = []
        # curr = head
        # while curr:
        #     arr.append(curr)
        #     curr = curr.next


        # l, r = 0, len(arr) -1

        # while l < r:
        # # [2,4,6,8,10]
        #     arr[l].next = arr[r]
        #     l+= 1
        #     if l >= r:
        #         break
        #     arr[r].next = arr[l]
        #     r -= 1

        #     arr[i].next = None
        if not head:
            return

        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        i, j = 0, len(nodes) - 1
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i >= j:
                break
            nodes[j].next = nodes[i]
            j -= 1

        nodes[i].next = None


        













        


























        # slow , fast = head, head.next

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # secondl = slow.next #the start of the second ll
        # prev = None
        # slow.next = None #i dont know why
        # while secondl:
        #     store = secondl.next #reuse
        #     secondl.next = prev
        #     prev = secondl
        #     secondl = store

        # #merge the two LL there will be storing of pointers
        # #define heads of both LL
        # #and store they're pointers

        # first, second = head, prev #can't use second cause it's None
        # while second:
        #     store1, store2 = first.next , second.next
        #     first.next = second
        #     #second = store1 #but this one failed can't we say second node points to first.next which is store 1
        #     second.next = store1
        #     first = store1
        #     second = store2






       