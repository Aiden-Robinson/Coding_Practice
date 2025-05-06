class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hashmap={}
        for i, num in enumerate(nums):#separates to index, value
            leftover= target- num
            if leftover in hashmap:
                return[hashmap[leftover],i]

            hashmap[num]=i

    
'''

Explanation

the key is to create a hashmap of all values and their index to prevent double indexing
the leftover is returned first because it would exist previously


'''