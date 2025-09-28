class Solution:
    def candy(self, ratings: List[int]) -> int:
        arr=[1]*len(ratings)


         #left to right pass
        for i in range(1, len(ratings)):
            if ratings[i]>ratings[i-1]:
                arr[i]= arr[i-1]+1
        
        #right to left pass

        for i in range(len(ratings)-2,-1,-1):
            if ratings [i]>ratings[i+1]:
                arr[i]= max(arr[i+1]+1, arr[i])
        
        return sum(arr)

            
#time complexity O(N)
#space complexity O(N)
            

        