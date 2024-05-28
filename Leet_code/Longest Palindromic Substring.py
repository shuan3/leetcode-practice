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
                    print(i,j)
                    dit[j-i]=s[i:j]
        print(dit)
        try:
            max(dit)
            return dit[max(dit)]
        except:
            return s[0]
s="bb"
Solution().longestPalindrome(s)


#slotion 2
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
                    Max_Len = j-i+1
                    Max_Str = s[i:j+1]

        return Max_Str
