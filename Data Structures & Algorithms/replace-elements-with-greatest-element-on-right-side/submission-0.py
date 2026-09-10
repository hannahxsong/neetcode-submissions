class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        right_max = 0
        #traverse array from right to left
        for i in range(len(arr) -1, -1, -1):
            if arr[i] > right_max:
                right_max = arr[i]
            arr[0] = -1


    

        arr[length-1] = -1

        return arr

        
        
            

        
        