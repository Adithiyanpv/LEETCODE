class Solution(object):
    def myPow(self, x, n):
        exp = 1
        if n < 0:
            flag = -1
        else:
            flag = 1
        n = abs(n)
        while n>0:
            if n%2 == 0:
                x = x*x
                n = n//2
            else:
                exp = exp*x
                n = n-1
        if flag == -1:
            return 1/exp
        else:
            return exp
#return x**n
#return math.pow(x,n)
        