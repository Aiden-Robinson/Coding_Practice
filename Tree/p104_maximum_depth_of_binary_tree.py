# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        res=0
        def dfs(node, count):
            nonlocal res
            if not node:
                return
            
            res= max(count, res)

            dfs(node.left, count+1)
            dfs(node.right, count+1)
        
        dfs(root,1)
        return res

#time complexity O(N)
#space complexity O(N), worst case the height is just a linked list 
            

        