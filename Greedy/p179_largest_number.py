class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        for i, n in enumerate(nums): #convert whole thing to string
            nums[i]= str(n)
        
        def compare(n1,n2): #will be as a string
            if n1+n2 >n2+n1:
                return -1
            else:
                return 1
            
        nums=sorted(nums, key= cmp_to_key(compare))
    
        return str(int("".join(nums)))

#time complexity O(NlogN)
#space complexity O(N)