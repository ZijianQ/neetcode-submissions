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
    int ans = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        
        dfs(root);
        return ans;

        
    }

    private int dfs(TreeNode n){
        if(n == null)return 0;
        int left = Math.max(0, dfs(n.left));
        int right = Math.max(0, dfs(n.right));

        ans = Math.max(ans, n.val + left + right);

        return n.val + Math.max(right, left);
    }
}
