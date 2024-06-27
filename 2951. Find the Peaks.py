class Solution:
    def findPeaks(self, mountain):
        l=[]
        for i in range(len(mountain)):
            if i==0 or i==len(mountain)-1:
                continue
            else:
                if mountain[i]>mountain[i-1] and mountain[i]>mountain[i+1]:
                    l.append(i)
        return l
