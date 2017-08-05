'''540 test'''
from math import sqrt

def CP(n):
    if n<5:
        return 0
    r=int(sqrt(n-1))
    while r*r>n-1:
        r-=1
    x,y=1,r/2*2
### points=[(x,y)]
    stk=[(0,2)]
    vx,vy=2,0
    A=0
    B=y
    while stk:
        while (x+vx)**2+(y-vy)**2<=n:
            x+=vx
            y-=vy
###         points.append((x,y))
            A+=vx*(2*y+vy)
            B+=2
        fnd=False
        cx,cy=stk.pop()
        while not fnd:
            while (x+cx)**2+(y-cy)**2<=n:
                stk.append((cx,cy))
                cx+=vx
                cy+=vy
            vx,vy=cx,cy
            if not stk:
                fnd=True 
                break
            cx,cy=stk.pop()
            while True:
                if (x+vx+cx)**2+(y-vy-cy)**2<=n:
                    #next point reached still within the circle
                    stk.append((cx,cy))
                    cx+=vx
                    cy+=vy
                    break
                #can the circle still be hit with a lesser slope from the outside point
                 # x+vx, y+vy that would be reached with the last cy/cx slope?
                if cx*(x+vx+cx)>=cy*(y-vy-cy): 
                    #no, therefore take the last valid value for vx,vy
                    vx,vy=cx,cy 
                    fnd=True
                    break
                #not yet optimal? proceed
                vx+=cx
                vy+=cy
    B+=y-x+1
    return (A+2*B)/8
### return points

     
#@cached({0:0,1:0,2:0,3:0,4:0})
def P(n):
    res=CP(n)
    sn=int(n**0.36)
    for i in xrange(1,sn+1):
        res-=P(n/(2*i+1)**2)   
    i2=i
    for j in xrange(n/(2*i+1)**2,0,-1):
        i=int(sqrt(n/j)-1)/2       
        res-=(i-i2)*P(j)
        i2=i
    return res

print(P(3141592653589793))