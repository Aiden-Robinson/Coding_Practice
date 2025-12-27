#include <unordered_set>
class Solution {
public:
  vector<int> findDisappearedNumbers(vector<int> &nums) {
    int n = nums.size();
    unordered_set<int> set;
    vector<int> res;
    for (const auto &num : nums) {
      set.insert(num);
    }

    for (int i = 1; i < n + 1; i++) {
      if (!set.count(i)) {
        res.push_back(i);
      }
    }

    return res;
  }
};
// time complexity O(N)
// space complexity O(N)