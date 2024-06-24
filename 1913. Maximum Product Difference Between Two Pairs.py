class Solution:
    def maxProductDifference(self, nums) -> int:
       nums.sort()
       print(nums)
       return nums[-1]*nums[-2] - nums[0]*nums[1]

nums = [5,6,2,7,4]
print(Solution().maxProductDifference(nums))


