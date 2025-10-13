class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        total = 0
        for boxes, units in boxTypes:
            if truckSize == 0:
                break
            take = min(boxes, truckSize)
            total += take * units
            truckSize -= take
        return total