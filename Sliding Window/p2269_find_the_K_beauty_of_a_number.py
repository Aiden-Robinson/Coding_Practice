class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:

        count=0

        #get it into a list for now

        nums=[]

        numTemp=num  #turning integer into a list of digits
        while numTemp>0:
            nums.append(numTemp%10)
            numTemp//=10
        
        nums=nums[::-1]  #reversing the list
        

        for i in range(len(nums)): #sliding window
            window=nums[i:i+k]
        
            number= int(''.join(map(str,window)))#turning the window into an integer
            if len(window)==k and number>0:
                if num%number==0:
                    count+=1

        return count 

#time complexiy O(k * Log num)
#space complexity O(k + Log num)
        
        


       



        
        