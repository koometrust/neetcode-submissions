# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #first pass to count the nodes
        if not head:
            return None

        count = 0
        currentNode = head
        while currentNode:
            count += 1
            currentNode = currentNode.next

        nthNode = count - n
       

        dummy = ListNode(0, head)
        currentNode = dummy
        counter2 = 0
        # for _ in range(nthNode):
        while counter2 < nthNode:
           counter2 += 1
           currentNode = currentNode.next
        currentNode.next = currentNode.next.next

        return dummy.next
            

            

            
            
            # # countForN += 1
            # if countForN == nthNode:
            #     #we skip nth Node
            #     dummyCurrent.next = dummyCurrent.next.next


    


            


































        # arr = []
        # curr = head
        # while curr:
        #     arr.append(curr) #what does memoey error mean
        #     curr = curr.next

        # val = len(arr) - n
        # if val == 0:
        #     return head.next
        
        # #we want to skip n
        # #we have the 

        # arr[val - 1].next = arr[val].next
        # return head





















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



         

         

         


        # while curr and curr.next:
        #     nodeToRemove = count - n
        #     countll += 1
        #     if nodeToRemove == countll:
        #         prev.next = curr.next
        #         # curr.next = curr.next.next
        #         prev = curr.next
        #         curr =  curr.next.next
        # return head.next








        
    




        