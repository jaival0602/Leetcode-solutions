# Last updated: 8/1/2025, 6:24:30 PM
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sum_digits(n):
            return sum(int(digit) for digit in str(n))

        digit_sum_pairs = []

        for number in nums:
            digit_sum = sum_digits(number)
            digit_sum_pairs.append((digit_sum, number))
            # print(digit_sum)
            # print(digit_sum_pairs)

        digit_sum_pairs.sort()

        max_pair_sum = -1

        for index in range(1, len(digit_sum_pairs)):
            current_digit_sum = digit_sum_pairs[index][0]
            previous_digit_sum = digit_sum_pairs[index - 1][0]

            if current_digit_sum == previous_digit_sum:
                current_sum = (
                    digit_sum_pairs[index][1] + digit_sum_pairs[index - 1][1]
                )
                max_pair_sum = max(max_pair_sum, current_sum)

        return max_pair_sum