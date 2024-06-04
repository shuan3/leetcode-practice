# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        count=0
        for end in range(1,len(s)+1):
            if len(set(s[start:end]))==len(s[start:end]):
                if (end-start+1)>count:
                    count=len(s[start:end])
            else:
                start+=1
        return(count)