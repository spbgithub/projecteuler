'''Problem 532'''
from numpy import cross, vdot, array, transpose, cos, sin, pi, sqrt, arccos
from numpy.linalg import solve
import matplotlib.pyplot as plt

def x(theta, alpha):
	return cos(theta)*sin(alpha)

def y(theta, alpha):
	return sin(theta)*sin(alpha)

def z(x, y):
	return sqrt(1 - x*x - y*y)

def path_len(pts):
	l = 0.0
	xold = x(pts[0][0], pts[0][1])
	yold = y(pts[0][0], pts[0][1])

	for j in range(1, len(pts)):
		#print(xold, yold, zold)
		xnew = x(pts[j][0], pts[j][1])
		ynew = y(pts[j][0], pts[j][1])
		l += sqrt((xold - xnew)**2 + (yold - ynew)**2 + (z(xold, yold) - z(xnew, ynew))**2)
		xold = xnew
		yold = ynew
	return l

def p(vec):
	return array([cos(vec[0])*sin(vec[1]), sin(vec[0])*sin(vec[1]), cos(vec[1])])

def q(vec, n):
	return p(array([vec[0] + 2*pi/n, vec[1]]))

def norm(vec):
	return sqrt(vdot(vec, vec))

def f(vec, n):
	a      = array([-sin(vec[0])*sin(vec[1]), cos(vec[0])*cos(vec[1]), cos(vec[0])*sin(vec[1]), sin(vec[0])*cos(vec[1]), 0, -sin(vec[1])]).reshape(3,2)
	pvec   = p(vec)
	v      = cross(q(vec, n), pvec)
	v      = v / norm(v)
	v      = cross(pvec, v)
	ata    = transpose(a).dot(a)
	return solve(ata, transpose(a).dot(v))

def rk45(vec, step, max_step, n):
	h = min(step, max_step)
	k1 = f(vec, n)
	k2 = f(vec + (h/2.0)*k1, n)
	k3 = f(vec + (h/2.0)*k2, n)
	k4 = f(vec + h*k3, n)
	return vec + (h/6.0)*(k1+2.*k2+2.*k3+k4)

def rk38(vec, step, max_step, n):
	h = min(step, max_step)
	k1 = f(vec, n)
	k2 = f(vec + (h/3.0)*k1, n)
	k3 = f(vec + h*k2 - (h/3.0)*k1, n)
	k4 = f(vec + h*k3 - h*k2 + h*k1, n)
	return vec + (h/8.0)*(k1+3.*k2+3.*k3+k4)

points = []
points.append(array([0.0, arccos(sqrt(1 - 0.999**2))]))

tolerance = 0.00001
num_bots  = 3
step      = 0.1
c = 0
while points[-1][1] > tolerance:
	max_step = norm(p(points[-1]) - q(points[-1], num_bots))/4.0
	points.append(rk38(points[-1], step, max_step, num_bots))

xvals = [x(u[0], u[1]) for u in points]
yvals = [y(u[0], u[1]) for u in points]
print(path_len(points))

plt.plot(xvals,yvals)
#for u in range(1, num_bots):
	#plt.plot(array(xvals)*cos(2*u*pi/num_bots) - array(yvals)*sin(2*u*pi/num_bots), array(xvals)*sin(2*u*pi/num_bots) + array(yvals)*cos(2*u*pi/num_bots))
plt.axes().set_aspect('equal', 'datalim')
plt.show()

