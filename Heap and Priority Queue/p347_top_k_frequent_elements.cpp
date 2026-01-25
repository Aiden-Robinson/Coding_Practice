
class Solution {
public:
  vector<int> topKFrequent(vector<int> &nums, int k) {
    // count it in a map
    vector<int> ans = {};
    unordered_map<int, int> map;

    // key= number, val= frequency
    for (int i = 0; i < nums.size(); i++) {
      map[nums[i]] += 1;
    }

    // append key values to priority queue (heap)
    priority_queue<pair<int, int>> pq;
    for (const auto &[num, freq] : map) {
      pq.push({freq, num});
    }
    // pop k times from heap
    for (int i = 0; i < k; i++) {
      auto top = pq.top();
      pq.pop();
      ans.push_back(top.second);
    }

    return ans;
  }
};