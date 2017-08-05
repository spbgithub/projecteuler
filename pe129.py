import time

def period_10_mod_n(n):
        per = 0
        q = 1
        while q  != 0:
                q  = q * 10 + 1
                per += 1
                q  = q % n
        return per

if __name__=="__main__":
        start = time.time()
        n = 1000001

        while True:
                if n % 5 != 0:
                        if period_10_mod_n(n) > 1000000:
                                print(n)
                                break
                n += 2
        print(time.time() - start)
