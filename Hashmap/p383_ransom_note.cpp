class Solution {
public:
  bool canConstruct(string ransomNote, string magazine) {
    unordered_map<char, int> noteMap;
    unordered_map<char, int> magMap;

    for (int i = 0; i < ransomNote.size(); i++) {
      noteMap[ransomNote[i]]++;
    }

    for (int i = 0; i < magazine.size(); i++) {
      magMap[magazine[i]]++;
    }

    for (const auto &[key, val] : noteMap) {
      if (magMap[key] < val) {
        return false;
      }
    }

    return true;
    ;
  }
};

// time complexity O(n+m)
// space complexity O(n+m)