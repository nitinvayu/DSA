class Solution:
    def sumZero(self, n: int) -> List[int]:
        sol = []
        if n%2!=0:
            sol.append(0)
            n-=1
        for i in range(1,n//2+1):
            sol.append(i)
            sol.append(-i)
        return sol
