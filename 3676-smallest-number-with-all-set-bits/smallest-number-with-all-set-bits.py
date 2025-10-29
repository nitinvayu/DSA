class Solution:
    def smallestNumber(self, n: int) -> int:
        l = len(bin(n))-2
        res = "1"*l
        return int(res,2)
