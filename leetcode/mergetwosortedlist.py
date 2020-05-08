# # Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    head = tail = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = ListNode(l1.val)
            tail,l1 = tail.next, l1.next
        else:
            tail.next = ListNode(l2.val)
            tail,l2 = tail.next,l2.next
    tail.next = l1 if l1 else l2
    return head.next