class Solution(object):
    def isIsomorphic(self, s, t):
        
        if len(s) != len(t):
            return False
        st1 = set(s)
        st2 = set(t)
        if len(st1) != len(st2):
            return False
        map1 = {}
        for ch1, ch2 in zip(s, t):
            if ch1 in map1:
                if map1[ch1] != ch2:
                    return False   
            else:
                map1[ch1] = ch2
        return True                
        