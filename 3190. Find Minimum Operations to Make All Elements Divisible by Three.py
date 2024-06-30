class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        r=0
        for i in nums:
            if i%3!=0:
                r+=1
        return r
