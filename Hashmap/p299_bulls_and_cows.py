class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        secHash=defaultdict(int)
        guessHash= defaultdict(int)

        Bull=0
        Cow=0

        #check for bulls while creating a freq table
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                Bull+=1
            
            else:
                secHash[secret[i]]+=1
                guessHash[guess[i]]+=1

        
        for c, val in guessHash.items():
            Cow+=min(guessHash[c],secHash[c])
        
        return f"{Bull}A{Cow}B"

#time complexity O(n)
#space complexity O(n)