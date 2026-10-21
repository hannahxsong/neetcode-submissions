class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #finding the complement
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [nums[complement], i]
            
            seen[complement] = i


            

                    

        
       