# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_num = ""
        sec_num = ""
        ret = None
        while l1:
            first_num += str(l1.val)
            l1 = l1.next
        while l2:
            sec_num += str(l2.val)
            l2 = l2.next
        sum = int(first_num[::-1]) + int(sec_num[::-1])
        new_sum = str(sum)
        for num in new_sum:
            new_node = ListNode(int(num), ret)
            ret = new_node
        return ret
        