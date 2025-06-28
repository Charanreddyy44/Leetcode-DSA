class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set([ch for ch in sentence.lower() if ch.isalpha()])) == 26

##
  #      return True        