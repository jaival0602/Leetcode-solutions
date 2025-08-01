# Last updated: 8/1/2025, 6:27:45 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        print(s)
        for i in s:
            if i.isalnum()==False:
                s=s.replace(i,"")
        return s==s[::-1]