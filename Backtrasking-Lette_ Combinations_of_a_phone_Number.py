from typing import List
# import config # type: ignore
# print('debug=%s'%config.debug)
# import os, sys

# #'/home/user/example/parent/child'
# current_path = os.path.abspath('.')

# #'/home/user/example/parent'
# parent_path = os.path.dirname(current_path)

# sys.path.append(parent_path)
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'child.settings')


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(idx, comb):
            if idx == len(digits):
                res.append(comb[:])
                return
class Solution:
    def __init__(self):
        self.default_dict={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],
                        '6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']
                        }
    def letterCombinations(self, digits: str) -> List[str]:
        final_list=[]
        d_list=[i for i in  str(digits)]
        if len(d_list)==1:
            # print("yes")
            return self.default_dict[digits]
        for i in range(len(d_list)):
            n_list=d_list.copy()
            n_list.pop(i)
            for j in range(len(n_list)):
                for ii in d_list:
                    for jj in n_list:
                        print(self.default_dict[i][ii],self.default_dict[j][jj])
                        final_list.append(self.default_dict[i][ii]+self.default_dict[j][jj])
        return final_list


    

print(Solution().letterCombinations("23"))
# print(Solution().default_dict)
# print("yes")
            
# k=[[1,1,1]]
# l=[1,2,3]
# k.extend([l])
# print(k)
# print(l[:])
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         if len(nums) == 1:
#             print(f" last is {nums}")
#             return [nums[:]]
        
#         res = []

#         for _ in range(len(nums)):
#             n = nums.pop(0)
#             perms = self.permute(nums)
                
#             for p in perms:
#                 p.append(n)
            
#             res.extend(perms)
#             print(f"n is {n}, perms is {perms}, _is {_},res is {res}")
#             nums.append(n)
        
#         return res
# print(Solution().permute([1,2,3]))
    