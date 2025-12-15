class Solution {
public:
  int minSubArrayLen(int target, vector<int> &nums) {
    int l = 0;
    int r = 0;
    int res = 1e9; // inifinity size

    cout << nums.size();

    int curSum = 0;
    while (r < nums.size()) {
      curSum += nums[r];
      while (curSum >= target) {
        res = std::min(res, r - l + 1);
        curSum -= nums[l];
        l += 1;
      }
      r += 1;
    }

    if (res == 1e9) {
      return 0;
    } else {
      return res;
    }
  }
};

// time complexity O(N)
// space complexity O(1)