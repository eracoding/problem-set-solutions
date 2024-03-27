# https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

# TIME LIMIT EXCEEDED SOLUTION
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        i, j, k = 0, 1, 2
        while i < len(nums) - 2:
            if nums[i] < nums[j] < nums[k]:
                return True
            if j == len(nums) - 2 and k == len(nums) - 1:
                i += 1
                j = i + 1
                k = j + 1
            elif k == len(nums) - 1:
                j += 1
                k = j + 1
            else:
                k += 1

        return False

# PROPOSED SOLUTION IN PYTHON
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True

        return False
