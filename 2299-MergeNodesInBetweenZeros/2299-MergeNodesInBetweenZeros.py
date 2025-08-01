# Last updated: 8/1/2025, 6:24:38 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        # fetch sum from current 0 to next 0
        ptr = head.next
        sum = 0
        while ptr.val != 0:
            sum += ptr.val
            ptr = ptr.next
        
        # assign sum on the first node between nodes having value 0
        head.next.val = sum
        
        # call and get the answer and connect the answer to next of head->next
        head.next.next = self.mergeNodes(ptr)
        
        # return head->next..=> new head
        return head.next
