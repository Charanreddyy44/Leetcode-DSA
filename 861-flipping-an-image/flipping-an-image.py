class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(image)
        for row in image:
            for i in range((n+1)// 2):
                row[i], row[n-1-i] = row[n-1-i] ^ 1, row[i] ^ 1
        return image     