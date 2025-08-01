# Last updated: 8/1/2025, 6:24:40 PM
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        # dp[i] will hold the maximum points from question i to the end.
        dp = [0] * (n + 1)  # dp[n] is 0 since there are no questions beyond n-1.
        
        # Process the questions in reverse order.
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            next_question = i + brainpower + 1
            # If the next question is within bounds, add dp[next_question]. Otherwise, add 0.
            solve = points + (dp[next_question] if next_question < n else 0)
            skip = dp[i + 1]
            dp[i] = max(solve, skip)
        
        return dp[0]