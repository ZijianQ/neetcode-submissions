# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if root: 
            queue.append(root)
        res = []
        while len(queue)>0:
            tem = []
            for i in range(len(queue)):
                curr = queue.popleft()
                tem.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
            res.append(tem)

        return res

                


        