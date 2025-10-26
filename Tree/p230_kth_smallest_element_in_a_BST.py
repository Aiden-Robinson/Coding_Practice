# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #in order traveral, left, center, right
        self.k=k
        self.result=0

        
        def dfs(node): #left, center, right -> in order traveral
            if not node:
                return
            
            dfs(node.left)

            self.k-=1
            if self.k==0:
                self.result=node.val
                return
            dfs(node.right)
        
        dfs(root)
        return self.result
  


# time complexity O(H+k)
# space complexity O(H)


