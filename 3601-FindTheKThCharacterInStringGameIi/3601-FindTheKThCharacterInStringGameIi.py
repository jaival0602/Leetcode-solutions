# Last updated: 8/1/2025, 6:23:39 PM
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n = len(operations)
        len_list = [1] * (n + 1)
        for i in range(1, n + 1):
            len_list[i] = len_list[i - 1] * 2

        def f(c):
            return 'a' if c == 'z' else chr(ord(c) + 1)

        def get_char(i, k):
            if i == 0:
                return 'a'
            if k <= len_list[i - 1]:
                return get_char(i - 1, k)
            else:
                if operations[i - 1] == 0:
                    return get_char(i - 1, k - len_list[i - 1])
                else:
                    c = get_char(i - 1, k - len_list[i - 1])
                    return f(c)

        result = get_char(n, k)
        return result