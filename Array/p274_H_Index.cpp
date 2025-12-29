class Solution {
public:
  int hIndex(vector<int> &citations) {
    int res = 0;
    sort(citations.begin(), citations.end());
    for (int i = 0; i < citations.size(); i++) {
      int remain = citations.size() - (i);
      res = max(res, min(citations[i], remain));
    }
    return res;
  }
};
// time complexity O(N logN)
// space complexity O(1)