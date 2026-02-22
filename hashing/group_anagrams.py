# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
#
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#
# Example 1:
#
# Input: strs = ["act","pots","tops","cat","stop","hat"]
#
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

#I could use the sorted word as a key and as a value

# I iterate through the list of strings once and add them to the hash and the new array at the same time

from collections import defaultdict
from typing import DefaultDict


class Solution:
    def group_anagrams(self, strings: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)
        for string in strings:
            sorted_strings = ''.join(sorted(string))
            anagrams[sorted_strings].append(string)
        return list(anagrams.values())
