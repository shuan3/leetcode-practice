# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.


# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.







from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            k = "".join(sorted(s))
            d[k].append(s)
        return list(d.values())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp_dict=dict()
        for i in strs:
            anagram=''.join(sorted(i))

            tmp_anagram=tmp_dict.get(anagram,[])
            tmp_anagram.append(i)
            tmp_dict[anagram]=tmp_anagram
            
            
        return tmp_dict.values()