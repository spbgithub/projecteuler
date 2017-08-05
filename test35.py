import time

def primes_sieve(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)

    return primes
    
def circular_number(num):
    number = str(num)
    l = len(number)
    c_num = []
    for i in range(l):
        x = ''
        for j in range(l):
            x += number[(i+j)%l]
        c_num.append(int(x))
    return c_num

start_time = time.time()
x = 1000000
primes = primes_sieve(x)

exclude = ['2','4','5','6','8','0']
req_primes =[2,3,5,7]

for p in primes:
    if p > 10:
        flag = 1
        for s in str(p):
            if s in exclude:
                flag = 0            
                break
            else:
                flag = 1
        if flag:
            req_primes.append(p)

ans = 0
a = []

for num in req_primes:
    
    c_num = circular_number(num)
    
    flag = 1
    for x in c_num:
        if x not in primes:
            flag = 0
            break
    
    if flag:
        ans += 1
        a.append(num)
        
stop_time = time.time()
        
print(ans)
print(stop_time - start_time)