'''
Created on Sep 3, 2019

@author: dchtk
''' 
def memoize(func):
    memo = dict()
    
    def decorated(n):
        if n not in memo:
            memo[n] = func(n)
        return memo[n]

    return decorated

@memoize
def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib_n = int(input("Fib number?"))
fibs = [fib(i) for i in range(fib_n)]
print (fibs)