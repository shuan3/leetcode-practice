# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first=second=float("inf")
        for n in nums:
            if n<=first:
                first=n
            elif n<=second:
                second=n
            else:
                return True
        return False