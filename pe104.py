#Problem 104#
from math import log10, sqrt

def is_uniqdig1to9(n):
    return '0' not in str(n) and len(set([u for u in str(n)])) == 9

#returns the nth fibonacci number and maintains a cache of nth fibonacci numbers as well
def fib(n, fiblist):
    if n in fiblist: return fiblist[n]
    if n % 2 == 0:
        fn2 = fib(n//2, fiblist)
        fn = fn2**2 + 2 * fn2 * fib((n//2)-1, fiblist)
    else:
        fn = fib((n//2)+1, fiblist)**2 + fib(n//2, fiblist)**2
    fiblist[n] = fn
    return fn
    

if __name__ == "__main__":
    modulus = 1000000000

    n = 1
    x = 0
    y = 1
    fiblist = {0:0, 1:1, 2:1}

    while True:
        x, y, n = y, (x + y) % modulus, n+1
        if is_uniqdig1to9(y):
            print("possibility found at n = ", n)
            ylong = fib(n, fiblist)
            fn = str(ylong)
            
            if is_uniqdig1to9(int(fn[0:9])):
                print("found it at n = ", n)
                break
            else:
                print("nope")
    print(n, fn[0:9], fn[-9:])


