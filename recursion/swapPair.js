var swapPairs = function(head) {
    node = head;
    helper(node);
    return head;
};

var helper = function(node){
    if (node && node.next){
        node2 = node.next;
        temp = node.val;
        node.val = node2.val;
        node2.val = temp;
        return helper(node2.next);
    }
}

var swapPairs2 = function(head) {
    if (head == null || head.next == null) return head;
 
     let dummy = head;
     let new_head = dummy.next;
     let prev = null;
 
     do {
         let next = dummy.next;
         dummy.next = next.next;
         next.next = dummy;
 
         dummy = dummy.next;
         if (prev == null) {
             prev = next.next;
         } else {
             prev.next = next;
             prev = next.next;
         }
 
     } while (dummy != null && dummy.next != null)
 
     return new_head;
 };