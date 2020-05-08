
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        edge case: head is empty
        
        copy node to its next 
        
        assign random node to the cloned node 
        
        unweave the current linked list and get back the original lsit and the clooned list 
        """
        if not head:
            return head
        ptr = head 
        
        while ptr:
            newNode = Node(ptr.val,None,None)
            newNode.next = ptr.next
            ptr.next = newNode 
            ptr = nexNode.next
        ptr = head 
        
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next 
        ptrOldList = head
        ptrNewList = head.next 
        headOld = head.next
        
        while ptrOldList:
            ptrOldList.next = ptrOldList.next.next
            ptrNewList.next = ptrNewList.next.next if ptrNewList.next else None
            ptrOldList = ptrOldList.next 
            ptrNewList = ptrNewList
        return headOld