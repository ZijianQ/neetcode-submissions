# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, maxSoFar: int):
            if not node: return 0
            count = 1 if node.val>= maxSoFar else 0
            maxSoFar  = max(maxSoFar, node.val)
            count += dfs(node.right, maxSoFar)
            count += dfs(node.left, maxSoFar)
            return count
        return dfs(root, float('-inf'))

        