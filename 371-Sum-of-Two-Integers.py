class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bit mask in hexadecimal
        mask = 0xffffffff
        
        # Works both as while loop and single value check 
        while (b & mask) > 0:
            
            carry = ( a & b ) << 1
            a = (a ^ b) 
            b = carry
        
        # Handles overflow
        return (a & mask) if b > 0 else a