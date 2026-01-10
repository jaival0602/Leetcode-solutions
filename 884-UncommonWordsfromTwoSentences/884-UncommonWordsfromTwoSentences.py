# Last updated: 1/9/2026, 10:32:06 PM
1class Solution:
2    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
3        dic={}
4        res=[]
5        s1=s1.split()
6        s2=s2.split()
7        for i in s1+s2:
8            if i in dic:
9                dic[i]+=1
10            else:
11                dic[i]=1
12        
13        for i in dic:
14            if dic[i]==1:
15                res.append(i)
16        return res
17