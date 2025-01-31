class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n=int(len(nums)/2)
        return nums[n]

from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_a={}
        for i in range(len(nums)):
            dict_a[nums[i]]=dict_a.get(nums[i],0)+1
        kk=max(v for v in dict_a.values())
        m=max(k for k in dict_a.keys() if dict_a[k]==kk)
        return m