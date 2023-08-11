# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode()
        dummy2 = ListNode()
        
        temp1, temp2 = dummy1, dummy2
        
        curr = head
        
        while curr:
            if curr.val < x:
                temp1.next = curr
                temp1 = curr
                
            else:
                temp2.next = curr
                temp2 = curr
            curr = curr.next
            
            
        temp1.next = None
        temp2.next = None
        temp1.next = dummy2.next
        return dummy1.next
        
            
        