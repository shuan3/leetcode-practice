from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        target_list=[]
        final_list=[]

        for i in range(len(nums)):
            if nums[i]==target:
                target_list.append(i)
        if len(target_list)==1:
            target_list.append(target_list[0])
            final_list=target_list
        elif len(target_list)>1:
            final_list.append(min(target_list))
            final_list.append(max(target_list))
        else:
            return [-1,-1]
        return final_list