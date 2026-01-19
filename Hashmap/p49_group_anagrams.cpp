class Solution {
public:
  vector<vector<string>> groupAnagrams(vector<string> &strs) {
    vector<vector<string>> output;
    unordered_map<string, vector<string>> map;

    for (auto &s : strs) {
      string temp = s;
      sort(s.begin(), s.end());
      map[s].push_back(temp);
    }

    for (const auto &[key, val] : map) {
      output.push_back(val);
    }

    return output;
  }
};

// time complexity O(N * K log K)
// space complexity O(N * K)