class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''
        for i in digits:
            string = string + str(i)
        number = int(string)+1
        res = str(number)
        result = []
        for i in res:
            result.append(int(i))
        return result