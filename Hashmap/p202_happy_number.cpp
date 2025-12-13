class Solution {
public:
  bool isHappy(int n) {
    unordered_set<int> seen;
    while (true) {
      if (seen.count(n)) {
        return false;
      }
      if (n == 1) {
        return true;
      }
      seen.insert(n);
      n = getDigSum(n);
    }
  }

  int getDigSum(int n) {
    int total = 0;
    while (n > 0) {
      total += (n % 10) * (n % 10);
      n = n / 10;
    }
    return total;
  }
};
// time complexity O(log N)
// space complexity O(log N)