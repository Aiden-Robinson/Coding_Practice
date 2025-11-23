class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #put everything in a set
        #iterate through again, run each number into the ground checking if its in the set

        res=0
        seen=set()

        for num in nums:
            seen.add(num)
        
        for num in seen:
            if (num-1) not in seen: #only check it if its the smallest in sequence
                window=0
                while num+window in seen:
                    window+=1
                    res=max(res,window)
        
        return res

#time complexity O(N)
#space complexity O(N)
