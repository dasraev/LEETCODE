class Solution:
    def commonChars(self, words):
        l = []
        str = set(words[0])
        n = len(words)
        d={}
        for s in str:  # b e l a
            d[s] = words[0].count(s)
        for i in d:
            r=1
            for word in words[1:]:
                if i in word:
                    if d[i]>word.count(i):
                        d[i]=word.count(i)
                    r+=1
            if r==n:
                for shit in range(d[i]):
                    l.append(i)
        return l



# words = ["bella","label","roller"]
words = ["cool","lock","cook"]
#c o

print(Solution().commonChars(words))





