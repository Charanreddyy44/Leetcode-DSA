class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        losses = {}
        for w, l in matches:
            losses[w] = losses.get(w, 0)
            losses[l] = losses.get(l, 0)+1
        no_loss = sorted([p for p in losses if losses[p] == 0])
        one_loss = sorted([p for p in losses if losses[p] == 1])
        return  [no_loss, one_loss]     