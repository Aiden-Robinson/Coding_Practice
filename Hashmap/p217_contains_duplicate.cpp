class Solution {
public:
  bool containsDuplicate(vector<int> &nums) {
    unordered_set<int> seen;
    for (const auto &num : nums) {
      seen.insert(num);
    }

    return nums.size() > seen.size();
  }
};

// time complexity O(N)
// space complexity O(N)