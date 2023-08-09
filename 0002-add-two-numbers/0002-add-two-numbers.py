# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def retrieveNumber(self, l: ListNode) -> int:
        num = ""
        while l:
            num += str(l.val)
            l = l.next

        num = num[::-1]
        return int(num)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        a = self.retrieveNumber(l1)
        b = self.retrieveNumber(l2)
        add = list(str(a + b))
        reverse_add = add[::-1]

        dummy = ListNode()
        temp = dummy

        for i in reverse_add:
            temp.next = ListNode(int(i))
            temp = temp.next

        return dummy.next

