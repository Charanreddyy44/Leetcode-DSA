class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        def remove_sub(s, a, b, points):
            stack = []
            total = 0
            for ch in s:
                if stack and stack[-1] == a and ch == b:
                    stack.pop()
                    total += points
                else:
                    stack.append(ch)
            return ''.join(stack), total

        total = 0
        if x > y:
            s, gain = remove_sub(s, 'a', 'b', x)
            total += gain
            s, gain = remove_sub(s, 'b', 'a', y)
            total += gain
        else:
            s, gain = remove_sub(s, 'b', 'a', y)
            total += gain
            s, gain = remove_sub(s, 'a', 'b', x)
            total += gain

        return total