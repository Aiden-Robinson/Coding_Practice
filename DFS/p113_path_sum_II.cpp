/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
public:
  vector<vector<int>> pathSum(TreeNode *root, int targetSum) {
    vector<vector<int>> ans;
    vector<int> curList;
    dfs(root, targetSum, ans, 0, curList);
    return ans;
  }

private:
  void dfs(TreeNode *node, int targetSum, vector<vector<int>> &ans, int curSum,
           vector<int> curList) {
    if (!node)
      return;

    curSum += node->val;
    curList.push_back(node->val);

    if (!node->left && !node->right) { // if its a leaf node
      if (curSum == targetSum) {
        ans.push_back(curList);
      }
      return;
    }

    dfs(node->left, targetSum, ans, curSum, curList);
    dfs(node->right, targetSum, ans, curSum, curList);
  }
};

// Time complexity O(N * H) where H is the height of the tree
// Space complexity O(H^2)
