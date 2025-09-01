class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prereq={c:[] for c in range(numCourses)}
      

        seen= set()

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        def dfs(crs):
            if prereq[crs]==[]: #no prerequisites to take
                return True
            if crs in seen:
                return False
            
            seen.add(crs)
            
            for pre in prereq[crs]:
                if not dfs(pre): 
                    return False
                
            seen.remove(crs)
            prereq[crs]=[] #marking it as valid
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True


#time complex O(V+E)
#space complex O(V+E)