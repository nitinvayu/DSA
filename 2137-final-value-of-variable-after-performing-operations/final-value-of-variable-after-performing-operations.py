class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for i in operations:
            if i[0] == '+' or i[-1] == '+':
                X += 1
            else:
                X -= 1
        return X