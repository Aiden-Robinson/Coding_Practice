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
  bool leafSimilar(TreeNode *root1, TreeNode *root2) {
    std::vector<int> ans1;
    std::vector<int> ans2;

    dfs(root1, ans1);
    dfs(root2, ans2);

    if (ans1 == ans2) {
      return true;
    } else {
      return false;
    }
  }

private:
  void dfs(TreeNode *node, vector<int> &sequence) {
    if (!node)
      return;

    if (!node->left && !node->right) { // if its a leaf node
      sequence.push_back(node->val);
      return;
    }

    dfs(node->left, sequence);
    dfs(node->right, sequence);
  }
};

// time complexity O(N+M)
// space complexity O(N+M)

// note: this is not an in order traversal because we are not doing anything
// with the internal nodes