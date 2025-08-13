class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = list(words[0])
        for word in words[1:]:
            temp = []
            for ch in res:
                if ch in word:
                    temp.append(ch)
                    word = word.replace(ch, "", 1)
                
            res = temp
        return res