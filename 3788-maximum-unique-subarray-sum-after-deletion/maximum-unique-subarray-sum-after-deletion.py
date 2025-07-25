class Solution:
    def maxSum(self, nums: List[int]) -> int:
        l=list(set(nums))
        s=0
        f=True
        for i in l:
            if i>0:
                s+=i
                f=False
        if f==True:
            return max(nums)
        return s