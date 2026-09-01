from collections import Counter
from itertools import islice
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #initialize result dict
        result_dict = Counter(nums)
        #iterate through array
        # Use sorted with a custom key to sort by frequency in descending order
        sorted_keys = sorted(result_dict.keys(), key=lambda x: result_dict[x], reverse=True)
        
        final_values = list(islice(sorted_keys, k))
        return final_values
