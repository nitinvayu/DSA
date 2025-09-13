class Solution:
    import collections
    def maxFreqSum(self, s: str) -> int:
        dict1 = collections.defaultdict(int)
        dict2 = collections.defaultdict(int)
        res=0
        for i in s:
            if i in['a','e','i','o','u']:
                dict1[i]+=1
            else:
                dict2[i]+=1
        max_vowel = max(dict1.values()) if dict1 else 0
        max_consonant = max(dict2.values()) if dict2 else 0
        return max_vowel + max_consonant