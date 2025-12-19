class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=0
        r= len(arr)-1

        while r-l+1>k: #stop when we reach a size of k

            if abs(x-arr[r])>=abs(x-arr[l]):
                r-=1
            else:
                l+=1
            print("this is l and r ", l,r)

        return arr[l:r+1]

#
#time complexity O(N)
#space complexity O(1)