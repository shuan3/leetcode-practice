class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1: return "1"
        if n==0: return ""
        s = [1]
        print(n, s)
        s[0] = 1
        d = None
        idx = 0
        nxt = 1
        i=0
        while True:
            c = s[i]
            if i == nxt:
                n -= 1
                if n == 1: break
                d = None
                nxt = len(s)
            if c != d:
                s.append(1)
                s.append(c)
                d = c
            else:
                s[-2] += 1
            i += 1
        return "".join([str(x) for x in s[nxt:]])
            



    #solution 2
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        s2 = ""
        for i in range(2 , n+1):
            count = 0
            curr = s[0]
            for c in s:
                if c == curr:
                    count += 1
                else:
                    s2+= str(count) + curr
                    count = 1
                    curr = c
            s2+= str(count) + curr
            print(s2)
            s = s2
            s2 = ""
        return s



# class Solution:         
#     def countAndSay(self, n: int) -> str:
        
#         s="1"
        
#         for num in range(1,n):
#                 Dict=dict()
#                 for i in str(s):
#                     Dict[i]=Dict.get(i,0)
#                     Dict[i]+=1
#                 print(Dict)
#                 s="".join([str(v)+k for k,v in Dict.items()])

#         return s




class Solution:         
    def countAndSay(self, n: int) -> str:
#         if n==1:
#             return "1"
        s="1"
#         print(pre_letter)
        s2=""
    
        for i in range(2,n+1):
            pre_letter=str(s)[0]
            frequency=0
            for letter in str(s):
                if letter==pre_letter:
                    frequency+=1
                else:
                    s2+= str(frequency) + pre_letter
#                     s2="".join([s2,str(frequency),str(letter)])
                    # print(f"s is {s}, frequency is {frequency}, letter is {letter} and s2 is {s2}")
                    frequency=1
                    pre_letter=letter
            s2+= str(frequency) + pre_letter
#                 s2="".join([s2,str(frequency),str(letter)])
            s = s2
            s2 = ""
        return s