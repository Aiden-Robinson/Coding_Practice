class TimeMap:

    def __init__(self):
        #self.time=0
        self.store={} #{key, (value, timestamp)}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.store:
            self.store[key]=[]
        self.store[key].append([value,timestamp])

        
    def get(self, key: str, timestamp: int) -> str:
        res=""

        values= self.store.get(key,[])

        l,r=0, len(values)-1
        

        while l<=r:
            mid= (l+r)//2
            if values[mid][1]<=timestamp: #search further up
                res= values[mid][0] #store at least a valid answer
                l=mid+1
            else: #search further down
                r=mid-1
        
        return res

    #time complexity O(LogN)
    #space complexity O(N)
    #space complexity   


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)