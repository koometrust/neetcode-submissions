# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        arr = []
        curr = head
        while curr:
            arr.append(curr) #what does memoey error mean
            curr = curr.next

        val = len(arr) - n
        if val == 0:
            return head.next
        
        #we want to skip n
        #we have the 

        arr[val - 1].next = arr[val].next
        return head






























        # # loop thru LL and add value to array
        # #remove the N-n index value.
        # # turn array into a LL
        # llArr = []
        # # for n in range(len(head)):
        # curr = head #whyyy
        # while curr: # i understand
        #     # llArr.append(n.val)
        #     llArr.append(curr)
        #     curr = curr.next


        # #remove the nth item e.g value at index 2
        # for i, v in enumerate(llArr):
        #     if i == len(llArr) - n:
        #         llArr.remove(v)          #   [1,2,3,4] len = 4+1 = 5   n = 2 = 3
        # return llArr

        # #turn LLARR into a LL

        # llArr = ListNode()


        # prev, curr = None, head
        # count = 0
        # countll = 0

        # while curr.next:
        #     count +=1
        # return count


        # while curr and curr.next:
        #     nodeToRemove = count - n
        #     countll += 1
        #     if nodeToRemove == countll:
        #         prev.next = curr.next
        #         # curr.next = curr.next.next
        #         prev = curr.next
        #         curr =  curr.next.next
        # return head.next








        
    




        