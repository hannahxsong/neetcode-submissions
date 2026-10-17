class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen:
                return true
            seen[num] = 1
        
        return false
    
            
        
        