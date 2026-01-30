class Solution(object):
    def mySqrt(self, x):
        ans = 0
        l,r = 0,x
        while l<=r:
            m = (l+r)//2
            if m*m == x:
                return m
            elif m*m >x:
                r = m-1
            else:
                ans = m
                l = m+1    
            
        return ans   


        