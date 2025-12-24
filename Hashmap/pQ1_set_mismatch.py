#include <unordered_set>
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
    
    unordered_set<int> hashset;
    int dup=0;
    int missing=0;

    for(const auto& num: nums){
        if (hashset.count(num)){
            dup=num;
        }
        hashset.insert(num);
    }

    for (int i=1; i<nums.size()+1; i++){
        if(!hashset.count(i)){
            missing=i;
        }
    }
    
    return {dup,missing};
    }
};
#time complexity O(N)
#space complexity O(N)