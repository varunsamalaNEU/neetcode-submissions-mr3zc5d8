from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # This dictionary will store: { (tuple_of_counts): [list_of_words] }
        # Example: { (1, 0, 1...): ["eat", "tea"] }
        ans = defaultdict(list)

        for s in strs:
            # 1. Create a frequency array of 26 zeros (one for each letter a-z)
            count = [0] * 26
            
            for char in s:
                # 2. Map the character to an index 0-25 
                # ord('a') is 97. If char is 'b' (98), 98 - 97 = index 1.
                count[ord(char) - ord('a')] += 1
            
            # 3. CONVERT TO TUPLE (The "Stone Tablet" step)
            # We must do this because lists cannot be dictionary keys.
            key = tuple(count)
            
            # 4. Append the word to the list matching this frequency key
            ans[key].append(s)
            
        # 5. Return only the values (the grouped lists)
        return list(ans.values())