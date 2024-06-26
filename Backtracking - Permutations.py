# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,s1]]
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        
        res = []

        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for p in perms:
                p.append(n)
            
            res.extend(perms)
            nums.append(n)
        
        return res
    


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ml = []

        def permutations(i):
            if i == len(nums):
                sl = []
                for n in nums:
                    sl.append(n)

                ml.append(sl.copy())
                return

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                permutations(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        permutations(0)
        return ml

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path): 
            if not nums: 
                result.append(path) 
                return 
            for i in range(len(nums)): 
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]]) 
        result = [] 
        backtrack(nums, []) 
        return result 
    



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, used): 
            if len(path) == len(nums): 
                result.append(path[:]) 
                return 
            for i in range(len(nums)): 
                if not used[i]: 
                    path.append(nums[i]) 
                    used[i] = True 
                    dfs(path, used) 
                    path.pop() 
                    used[i] = False 
        result = [] 
        dfs([], [False] * len(nums)) 
        return result 
    

class Solution:
    def permute(self,nums):
        n=len(nums)
        ans,sol=[],[]
        def backtrack():
            if len(sol)==n:
                ans.append(sol[:])
                return
            for x in nums:
                print(f"x is {x}, nums is {nums}, sol is {sol}, ans is {ans}")
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        backtrack()
        return ans
nums = [1,2,3]
Solution().permute(nums)


















#Permutation !!
# use hash map distionary
class Solution:
    def permute(self, nums):
        ans=[]
        sol=[]
        count={n:0 for n in nums}
        for n in nums:
            count[n]+=1
        def dfs():
            if len(sol)==len(nums):
                ans.append(sol.copy())
                return
            for n in count:
                if count[n]>0:
                    sol.append(n)
                    count[n]-=1

                    dfs()

                    count[n]+=1
                    sol.pop()
        dfs()
        return ans


