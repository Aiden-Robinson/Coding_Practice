class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not n: #an empty tree is a valid tree
            return True
        
        adjlist=defaultdict(list)

        for u,v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        
        seen= set()

        def dfs(i,prev):
            if i in seen:
                return False
            seen.add(i)
            for val in adjlist[i]:
                if val==prev:
                    continue
                prev= i
                if not dfs(val,prev):
                    return False
            return True #if it makes it all the way without a false
                
        return dfs(0,-1) and len(seen)==n
        
    
#time complexity O(V+E), each node is visited once each edge is visited at most twice
#space complexity O(V+E)


        