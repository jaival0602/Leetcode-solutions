# Last updated: 8/1/2025, 6:25:37 PM
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
            max_wealth = 0
            for i in accounts:
                curr_wealth = sum(i)
                if max_wealth < curr_wealth:
                    max_wealth = curr_wealth
            return max_wealth
