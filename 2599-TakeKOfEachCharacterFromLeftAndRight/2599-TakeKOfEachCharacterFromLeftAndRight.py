# Last updated: 8/1/2025, 6:24:21 PM
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        from collections import defaultdict

        n = len(s)
        count = {'a': 0, 'b': 0, 'c': 0}

        # Step 1: Count total occurrences of each character
        for c in s:
            if c in count:
                count[c] += 1

        # Step 2: Validate if it's possible to take k of each character
        for c in 'abc':
            if count[c] < k:
                return -1

        # Step 3: Compute prefix counts
        prefix = {'a': [0] * (n + 1), 'b': [0] * (n + 1), 'c': [0] * (n + 1)}
        for i in range(n):
            for c in 'abc':
                prefix[c][i + 1] = prefix[c][i] + (1 if s[i] == c else 0)

        # Step 4: Compute suffix counts
        suffix = {'a': [0] * (n + 1), 'b': [0] * (n + 1), 'c': [0] * (n + 1)}
        for y in range(1, n + 1):
            for c in 'abc':
                suffix[c][y] = suffix[c][y - 1] + (1 if s[n - y] == c else 0)

        # Step 5: Precompute min_y[c][t] for each character and required count
        min_y = {'a': [n + 1] * (k + 1),
                 'b': [n + 1] * (k + 1),
                 'c': [n + 1] * (k + 1)}
        
        for c in 'abc':
            y = 0
            for t in range(k + 1):
                # Find the minimal y where suffix[c][y] >= t
                while y <= n and suffix[c][y] < t:
                    y += 1
                if y <= n:
                    min_y[c][t] = y
                else:
                    min_y[c][t] = n + 1  # Impossible to satisfy

        # Step 6: Iterate over possible x and find the minimal x + y
        min_time = n + 1  # Initialize with a value greater than possible

        for x in range(n + 1):
            required = {}
            valid = True
            for c in 'abc':
                required[c] = max(0, k - prefix[c][x])
                if required[c] > k:
                    # Since required[c] cannot exceed k, this is just a safety check
                    valid = False
                    break
            if not valid:
                continue

            y_a = min_y['a'][required['a']]
            y_b = min_y['b'][required['b']]
            y_c = min_y['c'][required['c']]
            y = max(y_a, y_b, y_c)

            if y <= n - x:
                min_time = min(min_time, x + y)

        return min_time if min_time <= n else -1

