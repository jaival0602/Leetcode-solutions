# Last updated: 8/1/2025, 6:23:46 PM
class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        y = y // 4
        # taking minimum of x and y to know how many times we can make value 115
        x = min(x, y)
        # by modulo of x by 2 we find if it is equal to 1 Alice wins else Bob wins
        if x % 2 == 1:
            return "Alice"
        else:
            return "Bob"