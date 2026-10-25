# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        # O(n) time, O(1) space
        curr = head
        prev = None

        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev'''

        # O(n) time, O(n) space
        if head is None or head.next is None:
            return head

        curr = head
        
        if head.next:
            curr = self.reverseList(head.next)
            head.next.next = head

        head.next = None

        return curr
            
            
        