class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr)<3:
            return 0
    

        p=1
        res=0

        while p<len(arr):
            up=0
            down=0
            #going up
            while p<len(arr) and arr[p]>arr[p-1]:
                up+=1
                p+=1
            #going down
            while p<len(arr) and arr[p]<arr[p-1]:
                down+=1
                p+=1
            
            if up>0 and down>0:
                res= max(res, up+down+1) #up and down only count edges, we want nodes

            if p<len(arr) and arr[p]==arr[p-1]:
                p+=1
        return res


#time complexity O(N)
#space complexity O(1)  