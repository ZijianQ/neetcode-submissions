# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minNode(self, root:Optional[TreeNode]):
        cur = root
        while cur and  cur.left:
            cur = cur.left
        return cur
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None

        if root.val< key : 
            root.right = self.deleteNode(root.right, key)
        elif root.val> key : 
            root.left = self.deleteNode(root.left, key)

        else: 
            if not root.right: return root.left
            elif not root.left: return root.right
            else: 
                minval = self.minNode(root.right)
                succ = minval.val
                root.val = succ
                root.right = self.deleteNode(root.right, succ )

        return root


        