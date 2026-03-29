class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647
        
        res = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x:
            digit = x % 10
            x //= 10
            
            if res > (MAX - digit) // 10:
                return 0
                
            res = (res * 10) + digit
            
        return res * sign
