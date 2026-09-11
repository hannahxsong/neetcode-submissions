class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {
            ")":"(",
            "]":"[",
            "}":"{"

        }

        # whenever i see a closing braket, it must match the most recently opened bracket
        storage = []
    
        for i in s:
            # opening braket
            if i not in pairs:
                storage.append(i)
            # closing braket
            else:
                if not storage or storage[-1] != pairs[i]:
                    return False

                storage.pop()
        
        return len(storage) == 0
                      
                    

            


        

        