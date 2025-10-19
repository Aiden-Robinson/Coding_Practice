# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.secsmallest= float('inf')
        smallest= root.val

        def dfs(node):
            if not node:
                return

            if smallest<node.val<self.secsmallest:
                self.secsmallest=node.val 
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return self.secsmallest if self.secsmallest < float('inf') else -1
    
    #time complexity O(N)
    #space complexity O(H), height of tree