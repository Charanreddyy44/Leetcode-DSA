class Solution:
    def rotate(self, matrix):
        return [list(row) for row in zip(*matrix[::-1])]

    def findRotation(self, matrix, target):
        for i in range(4):
            if matrix == target:
                return True
            matrix = self.rotate(matrix)
        return False