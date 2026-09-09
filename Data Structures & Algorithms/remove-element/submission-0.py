class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        #initialize k
        k = 0

        #if the element isn't in array, change the element[0]
        
        for i in nums:
            if i != val:
                nums[k] = i
                k += 1
        return k 
            



        