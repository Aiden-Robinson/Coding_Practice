class Solution {
public:
  vector<vector<int>> merge(vector<vector<int>> &intervals) {
    sort(intervals.begin(), intervals.end());
    int i = 0;
    vector<vector<int>> res;
    while (i < intervals.size()) {
      int start = intervals[i][0];
      int end = intervals[i][1];
      while (i + 1 < intervals.size() && end >= intervals[i + 1][0]) {
        start = std::min(start, intervals[i + 1][0]);
        end = std::max(end, intervals[i + 1][1]);
        i++;
      }
      res.push_back({start, end});
      i++;
    }
    return res;
  }
};
// time complexity O(NLogN)
// space complexity O(N)