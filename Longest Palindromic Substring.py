# Given a string s, return the longest palindromic substring in s.

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Input: s = "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
#         start=0
#         end=len(s)-1
        dit=dict()
        if len(s)==1:
            return s
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j]==s[i:j][::-1]:
                    # print(i,j)
                    dit[j-i]=s[i:j]
        # print(dit)
        try:
            max(dit)
            return dit[max(dit)]
        except:
            return s[0]