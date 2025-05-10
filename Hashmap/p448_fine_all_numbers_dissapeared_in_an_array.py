class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n= len(nums)

        unique= set()

        for i in range (1,n+1):
            unique.add(i)
        
        for num in nums:
            unique.discard(num)

        return list(unique)

        #time complexity O(n)
        #space complexity O(n)
