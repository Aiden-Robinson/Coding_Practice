class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        #all we need to check for is the node that appears in two edge connections
        #the center node appears in every single connection entry
        a,b=edges[0]
        c,d=edges[1]

        if a==c or a==d:
            return a
        
        return b

    #time complexity O(1)
    #space complexity O(1)
