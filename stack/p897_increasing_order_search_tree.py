# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        stack=[]
        cur=root

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            stack.append(node)
            dfs(node.right)
        
        dfs(cur)

        
        dummy= TreeNode(-1)
        cur=dummy

        for node in stack:
            node.left=None #clear old left node
            node.right=None #clear old right node
            
            cur.right= node # point to current node
            cur= node #move pointer
        
        return dummy.right
#time complexity O(N)
#space complexity O(N), the extra list 
   