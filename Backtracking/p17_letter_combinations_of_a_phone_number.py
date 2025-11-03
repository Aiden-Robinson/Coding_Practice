class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return
        res=[]

        bank={
                "2":"abc",
                "3":"def",
                "4":"ghi",
                "5":"jkl",
                "6":"mno",
                "7":"pqrs",
                "8":"tuv",
                "9":"wxyz"
            }

        def backtrack(index, path): #path=[], index is for originally given number
            if len(path)==len(digits):
                res.append("".join(path))
                return
            
            cur_digit= digits[index]
            letters= bank[cur_digit]

            for letter in letters:
                path.append(letter)
                backtrack(index+1, path)
                path.pop()
            
        
        backtrack(0,[])

        return res

#time complexity O(4^N * N)
#space complexity O(N)