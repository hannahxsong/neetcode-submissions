from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #goal: group all anagrams together into sublists in any order
        #notes: we only care about the frequency of each letter in each string
        
        #initialize hashmap 
        result_dict = defaultdict(list)

        #iterate through the array
        for s in strs:
            freq_array = [0] * 26
            #iterate through each string
            for char in s:
                #update the frequency array
                freq_array[ord(char)-ord('a')] += 1
            #convert to tuple & use as key
            key = tuple(freq_array)
            #if char freq same, it's the same key!
            result_dict[key].append(s)
            
        #return the grouped anagrams
        return list(result_dict.values())
        
       