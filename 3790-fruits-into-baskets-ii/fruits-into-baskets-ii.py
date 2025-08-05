class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        unplaced = n

        for i in range(n):
            for j in range(n):
                if fruits[i] <= baskets[j]:
                    baskets[j] = 0
                    unplaced -= 1
                    break

        return unplaced 