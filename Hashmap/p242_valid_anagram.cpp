class Solution {
public:
  bool isAnagram(string s, string t) {
    unordered_map<char, int> mapS;
    unordered_map<char, int> mapT;

    for (const auto &c : s) {
      mapS[c] += 1;
    }

    for (const auto &c : t) {
      mapT[c] += 1;
    }

    if (mapS == mapT) {
      return true;
    }
    return false;
  }
};

// time complexity O(N)
// space complexity O(N)