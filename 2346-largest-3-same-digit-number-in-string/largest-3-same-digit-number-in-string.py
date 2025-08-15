class Solution:
    def largestGoodInteger(self, num: str) -> str:
        a=[]
        b=[]
        n=len(num)
        for i in range(1,n-1):
            if num[i-1]==num[i] and num[i]==num[i+1]:
                a.append(num[i])
        if len(a)==0:
            return ""
        else:
            return (str(max(a))*3 )