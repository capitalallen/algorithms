class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        prev, head, nextNode 
        1. head points to prev
        2. prev = head 
        3. head = head.next 
        """
        if not head or not head.next:
            return head;
        p = self.reverseList(head.next)
        head.next.next = head 
        head.next = None
        return p 