import random 
class RandomizedSet:

    def __init__(self):
        self.numMap={}
        self.numList=[]
        

    def insert(self, val: int) -> bool:
        res= val in self.numMap

        if res:
            return False
        else:
            self.numMap[val]= len(self.numList)
            self.numList.append(val)
            return True

    

    def remove(self, val: int) -> bool:
        res= val in self.numMap
        if res:
            inx= self.numMap[val]
            last= self.numList[-1]
            self.numMap[last]= inx
            self.numList[inx]=last
            self.numList.pop()
            del self.numMap[val]
            return True
        
        else:
            return False

    def getRandom(self) -> int:
        return choice(self.numList)
       


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()