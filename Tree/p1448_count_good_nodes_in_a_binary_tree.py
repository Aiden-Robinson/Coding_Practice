# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count=0
        def dfs(node,curPathMax):
            nonlocal count
            if not node:
                return
            
            curPathMax= max(curPathMax,node.val)
            if node.val>=curPathMax:
                count+=1
            
            dfs(node.left,curPathMax)
            dfs(node.right,curPathMax)

        dfs(root, root.val)
        return count
        
#time complexity O(N)
#space complexity O(H)