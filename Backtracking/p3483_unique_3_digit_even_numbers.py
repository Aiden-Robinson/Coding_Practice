class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans=set()

        def dfs(res, used): #string and an array of true false
            if len(res)==3:
                if res[0]!="0":
                    num=int(res)
                    if num%2 ==0:
                        ans.add(num)
            
                return

            for i in range(len(digits)):
                if not used[i]:
                    used[i]=True
                    dfs(res + str(digits[i]),used)
                    used[i]=False

        dfs("",[False]*len(digits))
        return len(ans)
      

#time complexity O(N^3)
#space complexity O(N)
       


       