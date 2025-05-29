class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        incoming= defaultdict(int)
        outgoing= defaultdict(int)

        for src, dst in trust:
            outgoing[src]+=1
            incoming[dst]+=1
        
        for i in range(1, n+1):
            if outgoing[i]==0 and incoming[i]==n-1:
                return i
        
        return -1

    #time complexity O(V+E), V is #nodes/vertices, E is # edges (might be diff than # nodes)
    #Space complexity O(V), because we make 2 hashmaps with all the nodes
        