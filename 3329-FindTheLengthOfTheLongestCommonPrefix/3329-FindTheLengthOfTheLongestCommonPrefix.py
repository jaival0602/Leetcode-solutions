# Last updated: 8/1/2025, 6:23:56 PM
class TreeNode:
    def __init__(self):
        self.children = dict()

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root = TreeNode()
        for num in arr1:
            num = str(num)
            curr = root
            for c in num:
                if c not in curr.children:
                    curr.children[c] = TreeNode()
                curr = curr.children[c]
        ans = 0
        for num in arr2:
            num = str(num)
            l = 0
            curr = root
            for c in num:
                if c not in curr.children:
                    break
                l += 1
                curr = curr.children[c]
            ans = max(ans,l)
        return ans