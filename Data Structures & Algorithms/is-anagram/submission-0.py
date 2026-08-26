class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        snum = len(s)
        tnum = len(t)
        if snum == tnum:
            seen_s = {}
            seen_t = {}
            for char in s:
                #looking for the key "char" in seen_s, and if it exists, return its value. otherwise, return 0. 
                seen_s[char] = seen_s.get(char, 0) + 1
            for char in t:
                seen_t[char] = seen_t.get(char, 0) + 1
            if seen_s == seen_t:
                return True
        return False