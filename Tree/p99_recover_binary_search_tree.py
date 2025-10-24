# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ans=[]
        def dfs(node): #in order traversal
            if not node:
                return
            dfs(node.left)
            ans.append(node)
            dfs(node.right)

        #who pointer anomaly detection
        dfs(root)
        
        first= None
        second=None

        for i in range(len(ans)-1):
            if ans[i].val>ans[i+1].val: #if a violation occurs
                if not first: #only setting it once
                    first= ans[i]
                
                second= ans[i+1]
        
        first.val,second.val=second.val,first.val

    #time complexity O(N)
    #space complexity O(N)  