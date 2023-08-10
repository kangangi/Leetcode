# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # get length of list
        temp = head
        count = 0
        while temp:
            temp = temp.next
            count += 1
    
        # create two pointers
        cur = head
        dummy = ListNode(0, cur)
        prev = dummy
    
        # loop to the nth node
        for _ in range(count - n):
            cur = cur.next
            prev = prev.next
            
        prev.next = cur.next
        cur.next = None
        
        return dummy.next
            
        
        
        