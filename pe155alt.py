import time
tStart = time.time()

def pgcd(a,b):
    while b: a, b = b, a % b;
    return a;

def rFraction(p,q):
    gcd=pgcd(p,q)
    return (p/gcd,q/gcd)

vect=[0,set([(1,1)])]
for nCapacitor in xrange(2,19):
    newState=set()
    for nombreCap1 in xrange(1,(nCapacitor/2)+1):
        for j in vect[nombreCap1]:
            for i in vect[nCapacitor-nombreCap1]:
                newState.add(rFraction(i[0]*j[1]+i[1]*j[0],i[1]*j[1]))
                newState.add(rFraction(i[0]*j[0],i[0]*j[1]+i[1]*j[0]))

    for i in vect[nCapacitor-1]:
        newState.add((i))
    vect.append(newState)
        
print len(newState)

print "Run Time = " + str(time.time() - tStart)