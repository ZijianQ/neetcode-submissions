 class Solution {
    public int goodNodes(TreeNode root) {
        return dfs(root, Integer.MIN_VALUE);  // ✅
    }

    private int dfs(TreeNode n, int max) {    // ✅
        if (n == null) return 0;
        int count = n.val >= max ? 1 : 0;
        max = Math.max(max, n.val);
        count += dfs(n.left, max);
        count += dfs(n.right, max);
        return count;
    }
}
