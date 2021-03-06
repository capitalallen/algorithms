/*** function TreeNode(val, left, right) {
    *     this.val = (val===undefined ? 0 : val)
    *     this.left = (left===undefined ? null : left)
    *     this.right = (right===undefined ? null : right)
    * }
    */
   /**
    * @param {TreeNode} root
    * @param {number} val
    * @return {TreeNode}
    */
   var searchBST = function(root, val) {
       if(root === null) {
           return null;
       }
       
       if(root.val === val) {
           return root;
       }
       
       return searchBST(root.left, val) || searchBST(root.right, val);
   };
   var searchBST2 = function(root, val) {
    
    if(root == null){
        return null;
    }
    
    if(val == root.val){
      return root;  
    }
    
    if(val < root.val){
       return searchBST(root.left,val);
    }else if( val > root.val){
      return searchBST(root.right,val);
    }
    
};