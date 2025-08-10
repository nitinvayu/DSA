class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if n==1:
            return True
        i=2
        l=[]
        while i<10**9:
            l.append(i)
            i*=2
        for num in l:
            if sorted(str(n))==sorted(str(num)):
                return True
        return False