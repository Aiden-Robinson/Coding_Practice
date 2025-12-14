class Solution {
public:
  bool isSubsequence(string s, string t) {
    int ps = 0;

    for (int i = 0; i < t.size(); i++) {
      if (t[i] == s[ps]) {
        ps += 1;
      }
    }

    // cout << ps;
    // cout << s.size()-1;
    if (ps == s.size()) { // if it made it to end
      return true;
    }

    return false;
  }
};

// time complexity O(N)
// space complexity O(1)