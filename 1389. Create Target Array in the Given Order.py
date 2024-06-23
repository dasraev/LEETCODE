class Solution:
    def createTargetArray(self, nums, index):
        target = []  # 0 1

        for i in range(len(index)):
            if index[i]<len(target):
                target = target[:index[i]] + [nums[i]] + target[index[i]:]
            else:
                target.append(nums[i])
        return target

nums = [0,1,2,3,4]
index= [0,1,2,2,1]

s=Solution()
print(s.createTargetArray(nums,index))
