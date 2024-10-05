class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        pattern = re.compile('\W')
        s = re.sub(pattern, '', s.lower())
        s=s.replace('_','')
        if s==s[::-1]:
            return True
        else:
            return False
        


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strippedString = ''.join(filter(lambda char : char.isalnum(), s.lower()))
        return strippedString == strippedString[::-1]
    


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "": return True
        
        s = ''.join([c for c in s if c.isalnum()])
        return s.lower() == s[::-1].lower()



class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        print(s)
        new_s=""
        for i in range(0,len(s)):
            if s[i].islower():
                new_s += s[i]
            elif s[i].isdigit():
                new_s += s[i]
        print(new_s)
        return new_s == new_s[::-1]