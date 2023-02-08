# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        head0 = ListNode(-1)
        head0.next = head
        root = head0
        while root.next !=None:
            if root.next.val ==val:
                root.next = root.next.next
            else:
                root = root.next
        return head0.next
        
