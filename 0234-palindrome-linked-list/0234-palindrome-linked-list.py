# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow = fast = head

        # find the middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #reverse the second half of the list
        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # see if the two halves are equal
        p1 = head
        p2 = prev

        while p2:
            if p1.val != p2.val:
                return False

            p2 = p2.next
            p1 = p1.next

        return True


        count = 1
        tail = head
        while tail.next:
            tail = tail.next
            count += 1

        print(count)
        if head.val == tail.val:
            return True
        return False
