class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        print(citations)

        h=0
        for i, c in enumerate(citations):
            if c >= i+1:
                h= i+1
        
        return h

    #time complexity O(N)
    #space complexity O(1)

        