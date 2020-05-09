class Solution:
    def swapPairs(self, head):     
        node1 = head
        def helper(node1):
            if node1 and node1.next:
                node2 = node1.next
                node1.val,node2.val = node2.val,node1.val 
                helper(node2.next)
        helper(node1)
        return head 

class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        first  = head
        second = head.next
        
        first.next = self.swapPairs(second.next)
        second.next = first
        
        
        return second