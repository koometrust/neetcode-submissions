# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy #why do we use tail instead of Dummy 

        # list1 = [1,2,4]

        # list2 = [1,3,5]


        # Output: [1,1,2,3,4,5]

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1 #tail.next points to the first node also isn't the first node Dummy, why are we using tail and tail means end so why is the begining of the merged soted array being called teh end or is it the tail of Dummy, why not just call it dummy.next
                list1 = list1.next #we create a pointer for the first node
            else: 
                tail.next = list2
                list2 = list2.next
            tail = tail.next #explain why this line existss
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next #explain how this is used to display the whole rest of the LInked list





        