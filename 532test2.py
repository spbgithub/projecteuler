from scipy.integrate import ode
from numpy import cross, array, transpose, cos, sin, tan, arctan2, pi, sqrt, arccos, arcsin, vdot
from numpy.linalg import solve
import matplotlib.pyplot as plt

num_bots = 3
start_radius = 0.99

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

def q(vec):
	return p([vec[0] + 2*pi/num_bots, vec[1]])

def norm(vec):
	return sqrt(vdot(vec, vec))

def f(t, vec):
	u = arctan2(-tan(pi/num_bots)*sin(vec[1]), 1)
	v = array([cos(u), -sin(u)])
	return v/norm(v)

y0, t0 = [0.0, arccos(sqrt(1 - start_radius**2))], 0
dt = 0.01

r = ode(f).set_integrator('dopri5')
r.set_initial_value(y0, t0)
tolerance = 0.0001
points = []
points.append(array(y0))

while r.successful() and r.y[1] > tolerance:
	r.integrate(r.t + dt)
	print(r.y)
	points.append(r.y)

xvals = [x(u[0], u[1]) for u in points]
yvals = [y(u[0], u[1]) for u in points]
zvals = [sqrt(1 - xvals[j]**2 - yvals[j]**2) for j in range(0, len(xvals))]
print(path_len(points))

plt.plot(xvals,yvals)
#for u in range(1, num_bots):
	#plt.plot(array(xvals)*cos(2*u*pi/num_bots) - array(yvals)*sin(2*u*pi/num_bots), array(xvals)*sin(2*u*pi/num_bots) + array(yvals)*cos(2*u*pi/num_bots))
plt.axes().set_aspect('equal', 'datalim')
plt.show()