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



# class Solution:
#     def group_anagrams(self, strings: List[str]) -> List[List[str]]:
#
#         anagrams = defaultdict(list)
#         for string in strings:
#             sorted_strings = ''.join(sorted(string))
#             anagrams[sorted_strings].append(string)
#         return list(anagrams.values())

from collections import defaultdict


# performant solution in O(n * m) where m is the number of strings 
# and n is the length of the longest string.
class Solution:
     def group_anagrams(self, strings: List[str]) -> List[List[str]]:
       
        anagram_dicts = defaultdict(list)
        for s in strs:
#
            count = [0] * 26
            for character in s:
                count[ord(character) - ord('a')] += 1
# this is equivalent to
# my_list = anagram_dicts[tuple(count)]
# my_list.append(s)
# tuples are used because they are immutable
            anagram_dicts[tuple(count)].append(s)
        return list(anagram_dicts.values())


groupAnagrams(["acat","pots","topsss","cata","ssstop","hat"])

