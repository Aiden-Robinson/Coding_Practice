# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:


        curSum=0

        def dfs(node,isLeft): #we can track whether the node is a left or right node 
            nonlocal curSum
            if not node:
                return
            if not node.left and not node.right and isLeft: #only sum if its a left leaf node
                curSum+=node.val
            dfs(node.left,True)
            dfs(node.right, False)
        
        dfs(root, False)
        return curSum
    
    #time complexity O(N)
    #space complexity O(h) , the call stack to get the height of the tree


            

        