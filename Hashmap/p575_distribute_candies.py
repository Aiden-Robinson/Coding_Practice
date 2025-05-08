class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """

        uniqueCandies= set(candyType) #goes thru each element once to build set 
        print(uniqueCandies)
        size= len(candyType)/2

        return min(size,len(uniqueCandies))

        #Time O (N), the time it takes to fill the set 
        #Space O(N), the size of the set, worst case all vals in array are 

        

