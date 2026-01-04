class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res=[0]*n
        stack=[]
        prevTime=0

        for log in logs:
            fid, typ, t= log.split(":")
            fid=int(fid)
            t=int(t)
           
            

            if typ=="start":
                if stack:
                    res[stack[-1]]+= t-prevTime
                stack.append(fid)
                prevTime=t
                
            else: #meaning it is end
                res[stack.pop()]+=t-prevTime+1
                prevTime=t+1
        
        return res
