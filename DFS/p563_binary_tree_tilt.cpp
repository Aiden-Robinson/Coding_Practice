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
  int findTilt(TreeNode *root) {
    totalTilt = 0;
    dfs(root);
    return totalTilt;
  }

private:
  int totalTilt;

  int dfs(TreeNode *node) {
    if (!node)
      return 0;

    int leftSum = dfs(node->left);
    int rightSum = dfs(node->right);

    int tilt = std::abs(leftSum - rightSum);
    totalTilt = totalTilt + tilt;

    return leftSum + rightSum + node->val;
  }
};

// time complexity O(N)
// space complexity O(h)
