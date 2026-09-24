class Solution:
    def sumSquares(self, num: int) -> int:
        sum = 0
        while num:
            digit = num % 10
            sum += digit ** 2
            num //= 10
        return sum
    
    def isHappy(self, n: int) -> bool:
        cycleSet = set()
        res = 0
        while res != 1:
            res = self.sumSquares(n)
            n = res
            if res == 1:
                return True
            elif res in cycleSet:
                return False
            
            cycleSet.add(res)




        