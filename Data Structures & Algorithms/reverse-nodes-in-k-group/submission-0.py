class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            tail = None
            while head:
                temp = head.next
                head.next = tail
                tail = head
                head = temp
            return tail

        # get length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        dummy_head = ListNode(0)
        curr = dummy_head
        
        while length >= k:
            # mark start of this group
            group_start = head
            
            # advance head k steps to start of next group
            # also track the tail of current group
            prev = None
            for _ in range(k):
                prev = head
                head = head.next
            
            # cut the group
            prev.next = None
            
            # reverse the group and attach to result
            curr.next = reverse(group_start)
            
            # advance curr to the tail of the just-reversed group
            # (which is group_start, since it's now the tail)
            curr = group_start
            
            # attach remaining list (will be overwritten next iteration if length >= k)
            curr.next = head
            
            length -= k
        
        return dummy_head.next
