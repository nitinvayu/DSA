class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        l = len(nums)
        c = 0
        left = 0
        right = sum(nums)
        for i in range(l):
            left+=nums[i]
            right -= nums[i]
            if nums[i]!=0:
                continue
            if left==right:
                c +=2
            if abs(left-right)==1:
                c +=1
        return c