class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = 0
        max_diag = 0
        for i in range(len(dimensions)):
            length = dimensions[i][0]
            width = dimensions[i][1]
            diag_sq = length**2 + width**2
            diag = math.sqrt(diag_sq)
            if diag > max_diag or (diag == max_diag and length * width > max_area):
                max_diag = diag
                max_area = length * width
        return max_area