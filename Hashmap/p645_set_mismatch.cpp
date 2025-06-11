class Solution {
public:
  vector<int> findErrorNums(vector<int> &nums) {

    int dup = 0;
    int rem = 0;
    unordered_map<int, int> hashmap;

    for (int i = 0; i < nums.size(); i++) {
      hashmap[nums[i]] += 1;
    }

    for (int i = 1; i < nums.size() + 1; i++) {
      if (hashmap.find(i) != hashmap.end()) {
        if (hashmap[i] > 1) {
          dup = i;
        }
      } else {
        rem = i;
      }
    }

    return {dup, rem};
  }
};

// time complexity O(N)
// space complexity O(N)