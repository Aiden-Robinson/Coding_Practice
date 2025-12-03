import random


class Solution:

    def __init__(self, nums: List[int]):
        self.hashmap={} #key = num, val= []
        for i, num in enumerate(nums):
            if num not in self.hashmap:
                self.hashmap[num]=[i]
            else:
                self.hashmap[num].append(i)
        

    def pick(self, target: int) -> int:
        choice= random.choice(self.hashmap[target])
        return choice