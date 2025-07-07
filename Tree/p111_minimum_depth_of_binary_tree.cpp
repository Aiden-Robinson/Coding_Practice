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
#include <climits>
class Solution {
public:
  int minDepth(TreeNode *root) {
    if (!root)
      return 0;
    int minLen = INT_MAX;
    dfs(root, 0, minLen);
    return minLen;
  }

private:
  void dfs(TreeNode *node, int curLen, int &minLen) {
    if (!node)
      return;

    curLen += 1;

    if (!node->left && !node->right) {
      minLen = std::min(minLen, curLen);
    }
    dfs(node->left, curLen, minLen);
    dfs(node->right, curLen, minLen);
  }
};

// time complexity: O(N)
// space complexity O(h), where h is the height of the tree