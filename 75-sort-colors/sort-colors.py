class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        p1=0
        p2=n-1
        cur=0
        while(cur<=p2):
            if nums[cur] == 0:
                nums[p1],nums[cur]=nums[cur],nums[p1]
                p1+=1
                cur+=1
            elif nums[cur] == 1:
                cur+=1
            elif nums[cur] == 2:
                nums[p2],nums[cur]=nums[cur],nums[p2]
                p2-=1