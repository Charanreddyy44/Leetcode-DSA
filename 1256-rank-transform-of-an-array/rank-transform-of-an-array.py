class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_nums = sorted(arr)
        ranks = {}
        rank = 1
        for x in sorted_nums:
            if x not in ranks:
                ranks[x] = rank
                rank += 1
        result = []
        for x in arr:
            result.append(ranks[x])
        return result    
