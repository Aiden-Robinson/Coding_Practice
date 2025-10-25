class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #connected nodes= n- #edges

        adjlist=defaultdict(list) #each node stores a list of where its pointing to

        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        
        #for an undirected graph, all edges appear twice
        count=0
        seen=set()

        def dfs(num):
            if num in seen:
                return
            
            seen.add(num)
            for nei in adjlist[num]:
                dfs(nei)
        
        for i in range(n):
            if i not in seen:
                count+=1
                dfs(i)
        
        return count
    
    #time complexity O(V+E), V is #nodes/vertices, E is # edges (might be diff than # nodes)
    #space complexity O(V), because we make a set to keep track of seen nodes