# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        if head is None:
            return None

        while curr :
            if curr.next and curr.next.val == curr.val :
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head