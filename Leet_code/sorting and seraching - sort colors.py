from typing import List
class Solution:
    def sortColors(self, arr: List[int]) -> None:
        n=len(arr)
        for i in range(n):
            for j in range(n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr
    



class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        t = len(nums)-1
        z = 0
        c = 0

        while c<=t:
            if nums[c]==2:
                nums[c],nums[t]=nums[t],nums[c]
                t-=1
            elif nums[c]==0:
                nums[c],nums[z]=nums[z],nums[c]
                z+=1
                c+=1
            else:
                c+=1

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        firstpointer = 0
        secondpointer = len(nums)-1
        movingpointer = 0

        while secondpointer >= movingpointer:
            if nums[movingpointer] == 0:
                nums[movingpointer], nums[firstpointer] = nums[firstpointer], nums[movingpointer]
                movingpointer += 1
                firstpointer += 1

            elif nums[movingpointer] == 2:
                nums[movingpointer], nums[secondpointer] = nums[secondpointer], nums[movingpointer]
                secondpointer -= 1

            else:
                movingpointer += 1

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.rainbow_sort(nums, 0, 0, len(nums) - 1)
        
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        
    def rainbow_sort(self, nums, left, mid, right):
        while mid <= right:
            if nums[mid] == 0:
                self.swap(nums, left, mid)
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                self.swap(nums, mid, right)
                right -= 1