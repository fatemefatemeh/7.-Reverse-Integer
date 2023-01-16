class Solution:
    def reverse(self, x: int) -> int:
        sign=1 if x>0 else -1
        
        x=abs(x)
        s=0
        while int(x) !=0:
            y=x%10
            x=x//10
            s=s*10+y
            if s>2**31-1:
                return 0
        
        return sign *s