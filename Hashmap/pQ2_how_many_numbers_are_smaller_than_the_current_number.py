class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
       #sort it
       #key = the number, val= how many less than
       #go through original array and use the mapping

       
        sortedNum=sorted(nums)
        # print(sortedNum)

        hashmap=defaultdict(int)
        prev=sortedNum[0]
        curCount=0
        for i in range(len(sortedNum)):
            if sortedNum[i]>prev:
                prev=sortedNum[i]
                hashmap[sortedNum[i]]=i
        
        res=[]
        for num in nums:
            res.append(hashmap[num])
        return res
    #time complexity O(N logN)
    #space complexity O(N)