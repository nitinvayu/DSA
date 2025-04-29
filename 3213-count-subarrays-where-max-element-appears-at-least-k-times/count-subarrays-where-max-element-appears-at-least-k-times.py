class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxi=max(nums)
        res=0
        l=0
        c=0
        for i in nums:
            if i==maxi:
                c+=1
            while c>=k:
                if nums[l]==maxi:
                    c-=1
                l+=1
            res+=l
        return res
