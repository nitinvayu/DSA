class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        count = 0
        max_cnt = 0
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                c=r-l+1
            else:
                while s[l]!=s[r]:
                    seen.remove(s[l])
                    l+=1
                l+=1
                c = r-l+1
            max_cnt = max(max_cnt,c)
        return max_cnt