# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def create_subset(i):
            if i == len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            create_subset(i+1)

            subset.pop()
            create_subset(i+1)

        create_subset(0)
        return res


# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

class Solution:
    def dfs(self,n:int,nums: List[int],subset:[],res:[]):
        if n>=len(nums):
            res.append(subset.copy())
            return
        subset.append(nums[n])
        self.dfs(n+1,nums,subset,res)
        subset.pop()
        self.dfs(n+1,nums,subset,res)        

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # nums=sorted(nums)
        # for i in nums
        subset=[]
        res=[]
        self.dfs(0,nums,subset,res)
        return res
            
  #best solution to understand
        
class Solution:
    def backtrack(self,res,temp_res,nums,n):       
        res.append(temp_res.copy())
        for i in range(n,len(nums)):
            print(f"i is {i} : n is {n} and res is {res} and temp_res is {temp_res}")
            temp_res.append(nums[i])
            self.backtrack(res,temp_res,nums,i+1)
            temp_res.pop(len(temp_res)-1)
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        temp_res=[]
        self.backtrack(res,temp_res,nums,0)
        
        return res
nums = [1,2,3]
Solution().subsets(nums)