class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    unordered_map<int, int> hashmap;
    for (int i = 0; i < nums.size(); i++) {
      int remain = target - nums[i];
      if (hashmap.count(remain)) {
        return {hashmap[remain], i};
      }
      hashmap[nums[i]] = i;
    }
    return {};
  }
};

// time complexity O(N)
// space complexity O(N)