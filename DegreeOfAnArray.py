class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #get frequency, first and last index maps
        freq={}
        first_index={}
        last_index={}

        for i in range(len(nums)):
            num= nums[i]
            freq[num]=freq.get(num,0)+1
            if num not in first_index:
                first_index[num]=i

            last_index[num]=i
        #get degree of the array
        degree=0
        for val in freq.values():
            degree= max(degree,val)

        #find minimum subarray length for elements with max degree
        min_length= len(nums)
        for num in freq:
            if freq[num]== degree:
                length= last_index[num]-first_index[num]+1
                min_length= min(min_length, length)
        
        return min_length
        
            
            


        