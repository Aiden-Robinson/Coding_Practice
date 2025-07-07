/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
  int maxDepth(Node *root) {
    int maxLen = 0;
    dfs(root, 0, maxLen);
    return maxLen;
  }

private:
  void dfs(Node *node, int curLen, int &maxLen) {
    if (!node)
      return;
    curLen += 1;
    if (node->children.empty()) { // if its a leaf node
      maxLen = std::max(curLen, maxLen);
      return;
    } else {
      for (Node *node : node->children) { // recurse over all of its children
        dfs(node, curLen, maxLen);
      }
    }
  }
};

// time complexity O(N)
// space complexity O(N)