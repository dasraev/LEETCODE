class Solution:
    def maxProduct(self, nums) -> int:
        r=1
        for i in range(2):
            r*=max(nums)-1
            nums.remove(max(nums))
        return r
