class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap=defaultdict(list)
        for a,b in prerequisites:
            hashmap[a].append(b)
        
        print(hashmap)

        visiting=set()
        visited=set()

        def dfs(num):
            if num in visiting:
                return False
            if num in visited:
                return True
            
            visiting.add(num)
            for val in hashmap[num]:
                if not dfs(val):
                    return False
            
            visiting.remove(num)
            visited.add(num)
                
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True



#time complex O(V+E)
#space complex O(V+E)
