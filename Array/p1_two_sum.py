class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap= defaultdict(int)

        for i in range(len(nums)):
            leftover= target-nums[i]
            if leftover in hashmap:
                return [hashmap[leftover],i]
            hashmap[nums[i]]=i

#time complexity O(N)
#space complexity O(N)

