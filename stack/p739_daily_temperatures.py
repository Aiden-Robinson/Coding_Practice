class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[] #store a pair [temp, index]

        for i,t in enumerate(temperatures):
            #clean up the stack
            while stack and t>stack[-1][0]:
                stackT, stackInd= stack.pop()
                res[stackInd]=(i-stackInd)
            stack.append([t,i])
        return res

    #time complexity O(N)
    #space complexity O(N)

    
    #brute force inefficient solution
        # res=[]
        # for i in range(len(temperatures)):
        #     for j in range(i, len(temperatures)):
        #         if temperatures[j]>temperatures[i]:
        #             res.append(j-i)
        #             break
        #         if j==len(temperatures)-1:
        #             res.append(0)
        
        # return res


