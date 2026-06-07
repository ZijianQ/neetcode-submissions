class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.right = None
        self.left = None
class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        
        newNode = TreeNode(key, val)

        if self.root == None:
            self.root = newNode
            return
        current = self.root
        while True:
            if key < current.key:
                if current.left == None:
                    current.left = newNode
                    return 
                current = current.left
            elif key > current.key:
                    if current.right == None:
                        current.right = newNode
                        return
                    current = current. right
            else:
                current.val = val
                return
        


    def get(self, key: int) -> int:
        current = self.root
        while current != None:
            if key< current.key:
                 current = current.left
            elif key > current.key:
                current = current. right
            else :    
                return current.val

        return -1

            

                


    def getMin(self) -> int:
        node = self.root
        while node and node.left:
            node = node.left

        return node.val if node else -1


    def getMax(self) -> int:
        node = self.root
        while node and node.right:
            node = node.right

        return node.val if node else -1



    def remove(self, key: int) -> None:
        self.root = self.rm_helper(self.root, key)
        

    def rm_helper(self, root, key):
        if not root: return None

        if key < root.key:
            root.left = self.rm_helper(root.left,key)
            return root
        if key > root.key:
            root.right =self.rm_helper(root.right,key)
            return root

        if not root.left: return root.right
        if not root.right: return root.left

        succ_parent = root
        succ = root.right

        while succ.left :
            succ_parent = succ
            succ= succ.left

        root.key, root.val = succ.key, succ.val

        if succ_parent.left == succ:
            succ_parent.left = succ.right
        else: 
            succ_parent.right = succ.right

        return root

        


    def getInorderKeys(self) -> List[int]:
        result: List[int] = []
        def dfs(root):
            if not root: return 
            dfs(root.left)
            result.append(root.key)
            dfs(root.right)

        dfs(self.root)

        return result




