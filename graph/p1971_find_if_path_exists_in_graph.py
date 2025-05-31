class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if source==destination:
            return True

        adjlist=defaultdict(list)
        
        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)

        seen=set()
        seen.add(source)

        def dfs(i):
            if i==destination:
                return True
            
            for nei_node in adjlist[i]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    if dfs(nei_node):
                        return True
            
            return False
        return dfs(source) 


#time complexity O(n+e)
#space complexity O(n+e)
        