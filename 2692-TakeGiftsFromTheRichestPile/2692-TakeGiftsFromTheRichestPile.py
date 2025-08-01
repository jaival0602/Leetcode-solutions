# Last updated: 8/1/2025, 6:24:16 PM
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        n = len(gifts)

        for _ in range(k):
            richest_pile_index = 0
            for currentPileIndex in range(n):
                if gifts[richest_pile_index] < gifts[currentPileIndex]:
                    richest_pile_index = currentPileIndex

            gifts[richest_pile_index] = math.floor(
                math.sqrt(gifts[richest_pile_index])
            )
        number_of_remaining_gifts = sum(gifts)

        return number_of_remaining_gifts