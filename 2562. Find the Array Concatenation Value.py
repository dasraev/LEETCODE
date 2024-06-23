class Solution:
    def findTheArrayConcVal(self, nums) -> int:
        s=0
        while len(nums)>0:
            if len(nums)>=2:
                s+=int(str(nums[0])+str(nums[-1]))
                nums.pop(0)
                nums.pop(-1)
            else:
                s += int(str(nums[0]))
                nums.pop(0)

        return s

nums = [5,14,13,8,12]

print(Solution().findTheArrayConcVal(nums))