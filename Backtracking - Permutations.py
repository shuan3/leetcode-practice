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