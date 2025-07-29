class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        n= len(nums)
        ans=0
        for i in range(n//3,n,2):
            ans+= nums[i]
        return ans