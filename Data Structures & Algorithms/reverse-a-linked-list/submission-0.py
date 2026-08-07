# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        dummy = ListNode(0)
        prev = dummy
        prev.next = curr
        while curr and curr.next:
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next