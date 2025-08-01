# Last updated: 8/1/2025, 6:24:30 PM
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        num_whites = 0
        num_recolors = k

        for right in range(len(blocks)):
            if blocks[right] == "W":
                num_whites += 1
            if right - left + 1 == k:
                num_recolors = min(num_recolors, num_whites)
                if blocks[left] == "W":
                    num_whites -= 1

                left += 1
        return num_recolors