# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxheight(self, root):
        if not root: return 0
        return 1+ max(self.maxheight(root.left),self.maxheight(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        leftHeight = self.maxheight(root.left)
        rightHeight = self.maxheight(root.right)
        diameter= leftHeight + rightHeight
        sub = max(self.diameterOfBinaryTree(root.right), self.diameterOfBinaryTree(root.left))
        return max(sub, diameter)

    
   