class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        """
        current_people = 0
        max_people = 0
    
        for ch in s:
            if ch == 'E':  
                current_people += 1
            else:  
                current_people -= 1
        
    
            max_people = max(max_people, current_people)
    
        return max_people
