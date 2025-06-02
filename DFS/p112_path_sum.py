# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        def dfs(node, curSum):
            if not node:
                return False

            curSum+=node.val
            
            if not node.left and not node.right: #indicates its a leaf node
                return curSum==targetSum
            
            return dfs(node.left,curSum) or dfs(node.right,curSum) #any one true will make it true
            
        
        return dfs(root,0)
    
    #time complexity O(N)
    #space compelxity O(N), for call stack worst case its just a linked list 

            
