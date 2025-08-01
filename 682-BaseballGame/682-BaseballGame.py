# Last updated: 8/1/2025, 6:26:23 PM
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scoresAdded = []
    
        for op in operations:
            if op.lstrip('-').isdigit(): 
                scoresAdded.append(int(op))
            elif op == 'C':
                scoresAdded.pop()
            elif op == 'D':
                scoresAdded.append(scoresAdded[-1] * 2)
            elif op == '+':
                scoresAdded.append(scoresAdded[-1] + scoresAdded[-2])

        return sum(scoresAdded)