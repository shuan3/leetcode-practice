# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lol=[]
        for i in range(len(nums)):
            l=nums[0:i]+nums[i+1::]
            h=1
            for j in l:
                h=j*h
            lol.append(h)
        return lol

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        product = 1 
        single_zero = False 
        multiple_zeros = False 

        #gets the total product 
        for num in nums:
            if num == 0 and not single_zero :
                single_zero = True 
            elif num == 0 and single_zero:
                multiple_zeros = True 
            else:
                product *=num
        
        output_array = []
        #makes the returned array
        

        if multiple_zeros:
            return [0] * len(nums)
        elif single_zero:
            for num in nums:
                if num == 0:
                    output_array.append( product ) 
                else:
                    output_array.append(0) 
        else:
            for num in nums:
                output_array.append( product/num )

        return output_array 