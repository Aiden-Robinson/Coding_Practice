class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        goodIndex= set()

        for t in triplets:
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2]:
                pass
        
            for i, val in enumerate(t):
                if val==target[i]:
                    goodIndex.add(i)
            
        
        if len(goodIndex)==3:
            return True
        else:
            return False

#time complexity O(N)
#space complexity O(1)