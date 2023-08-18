# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        queue = []

        if head is None:
            return False

        curr = head
        while curr:
            queue.append(curr.val)
            curr = curr.next
        
        print(queue)
        curr = head
        while queue:
            if queue.pop() != curr.val:
                return False
            curr = curr.next  
        return True

    
