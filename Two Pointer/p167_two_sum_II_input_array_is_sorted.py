class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        r= len(numbers)-1
        l=0

        while l<=r:
            total= numbers[r]+numbers[l]

            if total>target:
                r-=1
            
            elif total<target:
                l+=1
            
            else:
                return [l+1,r+1]

#time complexity O(N)
#space complexity O(1)
