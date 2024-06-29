class Solution:
    def totalMoney(self, n: int) -> int:
        d=0
        r=1
        for i in range(1,n+1):
            if (i-1)%7==0 and i!=1:
                r=i//7+1
            d+=r
            r+=1
        return d