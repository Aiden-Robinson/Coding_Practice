# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p,q):
            if not p and not q:
                return True

            if p and q and p.val==q.val:
                return dfs(p.right, q.right) and dfs(p.left, q.left)
            
            return False #will stop recursion if above check is not true
        
        return dfs(p,q)

#time complexity O(N) , number of nodes in smaller tree
#space complexity O(h), recursive call of the stack

