# Last updated: 1/8/2026, 12:11:04 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        st = []
4        res = [0] * len(temperatures)
5
6        for i in range(len(temperatures)):
7            while st and temperatures[i] > temperatures[st[-1]]:
8                idx = st.pop()
9                res[idx] = i - idx
10            st.append(i)
11        
12        return res