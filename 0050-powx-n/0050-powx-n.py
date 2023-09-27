# class Solution:
#     def myPow(self, x: float, n: int) -> float:
        
#         def recursiving(num, power, total):
#             if power == 0: 
#                 return total
#             if power < 0:
#                 num = 1 / num
#                 power = -power
#             return recursiving(num, power-1, total*num)
        
#         return recursiving(x, n, 1)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case: If the power is 0, return 1
        if n == 0:
            return 1

        # Base case: If the power is 1, return x
        if n == 1:
            return x

        # If n is negative, invert x and change n to positive
        if n < 0:
            x = 1 / x
            n = -n

        # Recursive case: Divide and conquer, reducing the power by half
        half_pow = self.myPow(x, n // 2)

        # If n is even, return half_pow squared
        if n % 2 == 0:
            return half_pow * half_pow
        # If n is odd, return half_pow squared times x
        else:
            return half_pow * half_pow * x