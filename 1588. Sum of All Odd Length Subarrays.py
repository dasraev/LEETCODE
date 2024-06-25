class Solution:
    def sumOddLengthSubarrays(self, arr):
        n=len(arr)
        if n%2==0:
            l=list(range(1,n,2))
        else:
            l=range(1,n+1,2)
        print(l)
        r=0
        for i in l: #1,3,5
            for j in range(len(arr)):
                if (j+i)>n:
                    break
                r+=sum(arr[j:(j+i)])
        return r