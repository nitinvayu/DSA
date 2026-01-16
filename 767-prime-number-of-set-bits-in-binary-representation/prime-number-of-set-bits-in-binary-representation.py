class Solution:
    def is_prime(self,n):
        c = 0
        if n == 0 or n ==1:
            return False
        elif n ==2:
            return True
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        if left == 0:
            left+=1
        for i in range(left,(right+1)):
            c = 0
            temp = i
            while temp!=0:
                if (temp&1) == 1:
                    c+=1
                temp = temp>>1
            if self.is_prime(c)==True:
                ans+=1
        return ans