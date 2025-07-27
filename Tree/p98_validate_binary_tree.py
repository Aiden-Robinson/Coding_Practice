# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node,lb, rb): #left bound and right bound
            if not node:
                return True
            
            if not(node.val>lb and node.val<rb):
                return False
            
            return dfs(node.right, node.val, rb) and dfs(node.left,lb, node.val)
        

        return dfs(root, float('-inf'), float('inf'))
        
#time complexity O(N), each node is visited once 
#space complexity O(H), recursive call stack

        


        

        

        