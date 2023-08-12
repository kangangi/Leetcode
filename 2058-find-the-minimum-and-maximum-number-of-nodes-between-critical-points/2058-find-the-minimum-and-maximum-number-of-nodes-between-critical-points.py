# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        prev = head
        temp = head.next
        index = []
        count = 2

        while temp and temp.next:
            if (prev.val > temp.val and temp.next.val > temp.val) or (prev.val < temp.val and temp.next.val < temp.val):
                index.append(count)
            prev = temp
            temp = temp.next
            count += 1
            
        if not (len(index) > 1 or temp.next):
            return [-1, -1]
        
            
        maximum = index[-1] - index[0]
        minimum = [index[i+1] - index[i] for i in range(len(index)-1)]
        
        return [min(minimum), maximum]
        