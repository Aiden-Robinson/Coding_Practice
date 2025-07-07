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
  int getMinimumDifference(TreeNode *root) {
    int minDiff = 1e9; // basically infinity
    TreeNode *prev = nullptr;
    dfs(root, prev, minDiff);

    return minDiff;
  }

private:
  void dfs(TreeNode *node, TreeNode *&prev,
           int &minDiff) { // prev is a reference to a pointer
    if (!node)
      return;

    dfs(node->left, prev,
        minDiff); // in order traversal with left, root, right for binary trees

    if (prev) {
      minDiff = std::min(node->val - prev->val,
                         minDiff); // prev is gaurantee to be less than node val
    }

    prev = node;

    dfs(node->right, prev, minDiff);
  }
};
// time complexity O(N)
// space complexity O(N)
