# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return
            
            temp=node.right
            node.right=node.left
            node.left=temp

            dfs(node.left)
            dfs(node.right)

            return node

        return dfs(root)

#time complexity O(N)
#space complexity O(H), H is the height of the tree
