from typing import List
from collections import Counter

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suffix_counter = Counter(nums)   # counts of all elements in suffix
        prefix_set = set()
        res = []

        for num in nums:
            # move num from suffix -> prefix
            prefix_set.add(num)
            suffix_counter[num] -= 1
            if suffix_counter[num] == 0:
                del suffix_counter[num]

            # compute difference
            res.append(len(prefix_set) - len(suffix_counter))

        return res

        #time complexity O(N)
        #space complexity O(N)