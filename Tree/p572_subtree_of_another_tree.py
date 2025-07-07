# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))

    

    def sameTree(self, t, s):
        if not t and not s:
            return True

        if s and t and s.val==t.val:
            return self.sameTree(t.left,s.left) and self.sameTree(t.right, s.right)
        
        return False
        

    #time complexity O(N*M)
    #space complexity O(N+M)