/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public boolean isValidBST(TreeNode root) {
        return checkBST(root, Integer.MIN_VALUE,Integer.MAX_VALUE);
        
    }
    private boolean checkBST(TreeNode n, int min, int max ) {
        if (n == null) return true; 
        if (n.val <= min|| n.val >= max)return false;
        
        return checkBST(n.left, min, n.val)&& 
        checkBST(n.right,n.val, max);

        
    
    
        
    }

}

    
