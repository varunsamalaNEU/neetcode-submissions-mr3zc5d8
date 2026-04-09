class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count = {}
        for c in s:
            if c not in count:
                count[c] = 1
            else: 
                count[c] += 1
        count_t = {}
        for c in t:
            if c not in count_t:
                count_t[c] = 1

            else:
                count_t[c] += 1

        return count == count_t
