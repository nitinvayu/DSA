class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        left = right = 0
        ans = 0
        while(left<n and right<n):
            if nums[left]!=0:
                left+=1
            elif nums[left]==0:
                right=left
                while(right<n and nums[right]==0):
                    right+=1
                    ans+=right-left
                left=right   
        return ans
