class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n=0
        prev_i=''
        for i in range(len(s)):
            if s[i]!=' ' and prev_i!=' ':
                n+=1
            elif s[i]!=' ' and prev_i==' ':
                n=0
                n+=1
            prev_i=s[i]
        return n