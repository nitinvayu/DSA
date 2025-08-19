class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        left = right = 0
        d=defaultdict(int)
        while(left<n and right<n):
            if nums[left]!=0:
                left+=1
            elif nums[left]==0:
                right=left
                while(right<n and nums[right]==0):
                    right+=1
                d[right-left]+=1
                left=right
        ans=0
        for k,v in d.items():
            ans+=((k*(k+1)//2)*v)
        return ans
