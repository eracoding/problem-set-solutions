# https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = [1] * n

        for i in range(n-2, -1, -1):
            a[i] = a[i+1] * nums[i+1]
        
        b = 1
        for i in range(1, n):
            b *= nums[i-1]
            a[i] *= b
        return a

# My?
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * n
        sufix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            sufix[i] = sufix[i+1] * nums[i+1]
        return [a[0] * a[1] for a in zip(prefix, sufix)]
