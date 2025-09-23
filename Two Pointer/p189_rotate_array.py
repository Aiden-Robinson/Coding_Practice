class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
    
        def reverse (arr,l,r):
            while l<r:
                arr[l],arr[r]= arr[r],arr[l]
                l+=1
                r-=1
        

        reverse(nums,0,n-1)
        reverse(nums,0, k-1)
        reverse(nums, k, n-1)

       
#time complexity O(N)
#space complexity O(1)
    
       
    #time complexity O(N)
    #space complexity O(N)
    #can be improvedb by doing it in place with pointers


        # n=len(nums)
        
        # k= k%n

        # end= nums[n-k:]
        # start= nums[:n-k]
        # nums[:]= end+start

