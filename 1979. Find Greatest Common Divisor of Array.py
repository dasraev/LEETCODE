class Solution:
    def findGCD(self, nums) -> int:
        a=max(nums)
        b=min(nums)
        while a%b!=0:
            a,b=b,a%b
        return b


