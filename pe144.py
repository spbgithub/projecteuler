'''Problem 144'''


#from fractions import Fraction
from decimal import *

getcontext().prec = 30

def new_dy(dx0,dy0,dx,dy):
	return -dx0**2 * dy + 2 * dx * dx0 * dy0 + dy * dy0**2

def new_dx(dx0,dy0,dx,dy):
	return 2*dx0*dy*dy0 + dx*(dx0-dy0)*(dx0+dy0)

def new_xy(dx0,dy0,x0,y0):
	if dx0 == 0:
		return x0, -y0
	if dy0 == 0:
		return -x0, y0

	m0 = dy0/dx0
	new_x = (Decimal(2)*m0**2*x0 - Decimal(2)*m0*y0)/(Decimal(4)+m0**2) - x0
	new_y = y0 + m0*(new_x - x0)
	#ratio = Decimal(10.0)/Decimal(4*new_x**2 + new_y**2).sqrt()
	return new_x, new_y


dx    = Decimal(1.4)
dy    = Decimal(-9.6-10.1)
x     = Decimal(1.4)
y     = Decimal(-9.6)
dxtan = Decimal(y)
dytan = Decimal(-4*x)
n     = 1

while not(abs(x) <= 0.01 and y > 0):
	dxnew = new_dx(dxtan,dytan,dx,dy)
	dynew = new_dy(dxtan,dytan,dx,dy)
	x, y = new_xy(dxnew,dynew, x, y)
	dx, dy = dxnew, dynew
	dxtan, dytan = y, Decimal(-4)*x
	n += 1
	#print(n,float(x), float(y), float(4*x**2 + y**2))
	print(n,x,y,4*x**2 + y**2)
print(n)
