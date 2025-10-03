class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        i=0
        while i < len(nums):
            combo=f"{nums[i]}"

            while i+1< len(nums) and nums[i]+1==nums[i+1]:
                combo.join("->")
                combo.join(f"{nums[i+1]}")
                i+=1
            
            res.append(combo)
            

            i+=1
        
        return res


        