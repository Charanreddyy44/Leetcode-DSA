class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        num = 0
        l = 0
        while True:
            num = (num*10+1) % k
            l +=1
            if num == 0:
                return l 

     #   res = '1'* k
     #   ans = int(res)
     #   if ans % k == 0:
    #     return len(res)
     #   else:
     #       return -1    
        