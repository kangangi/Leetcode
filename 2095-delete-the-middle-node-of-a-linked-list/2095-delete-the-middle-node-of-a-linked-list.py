# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        fast, slow = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        if not prev:
            head = None
        else:
            prev.next = slow.next
            slow.next = None
        return head

        