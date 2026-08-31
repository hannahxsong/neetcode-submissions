class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap to store output indices
        seen = {} 
        # iterate through the array nums & obtain both the index and the value
        for i, value in enumerate(nums): 
            #subtract the element from the target
            complement = target - value
             #check for the complement in array
             #code processes nums left to right, so smallest index is always 
            if complement in seen:
                return [seen[complement],i]
            
            #storing values and their respective index in hashmap
            seen[value] = i
       