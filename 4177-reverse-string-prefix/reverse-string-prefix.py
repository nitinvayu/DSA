class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        res=[]
        for i in range(k-1,-1,-1):
            res.append(s[i])
        for j in range(k,len(s)):
            res.append(s[j])
        return "".join(map(str,res))