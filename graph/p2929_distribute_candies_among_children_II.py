class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:

        ans=0
        
        for c1 in range(min(n,limit)+1):
            remain_c2_c3= n-c1

            if remain_c2_c3<0:
                continue

            min_c2= max(0,remain_c2_c3-limit)
            max_c2=min(limit, remain_c2_c3)

            if max_c2>= min_c2:
                ans+= (max_c2-min_c2+1)
            
        return ans

#Time complexity O(min(n,limit))
#Space complexity O(1)
        