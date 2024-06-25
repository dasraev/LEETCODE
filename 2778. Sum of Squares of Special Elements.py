class Solution:
    def sumOfSquares(self, nums) -> int:
        n = len(nums)
        r = 0
        for i in range(len(nums)):
            if n % (i + 1) == 0:
                r += nums[i] * nums[i]
        return r

