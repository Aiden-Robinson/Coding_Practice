class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[]
        n=len(nums)

        hashmap= defaultdict(int)

        for num in nums:
            hashmap[num]+=1
        
        for key, value in hashmap.items():
            if value> n/3:
                res.append(key)
            
        return res

#could me more efficnet
#time O(NlogN)
#space O(N)
