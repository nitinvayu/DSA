class Solution:
    def findLucky(self, arr: List[int]) -> int:
        map = dict()
        for item in arr:
            if item in map.keys():
                map[item] += 1
            else:
                map[item] = 1
        #print(map.items())
        largest = -1
        for key,value in map.items():
            if key == value and key>largest:
                largest = value
        return largest