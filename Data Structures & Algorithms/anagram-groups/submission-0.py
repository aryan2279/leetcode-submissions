from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using a defaultdict to automatically handle new keys
        res = defaultdict(list)

        for s in strs:
            # Create a frequency count array for letters 'a' through 'z'
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            # Convert the list to an immutable tuple so it can be used as a dictionary key
            res[tuple(count)].append(s)

        # Return just the grouped lists of anagrams
        return list(res.values())
        