def subset(l, prefix):
	if len(l) == 0:
		return [prefix]
	else:
		return subset(l[1:], prefix + [l[0]]) + subset(l[1:], prefix)

def subset_n(l, n, prefix):
	if n == 0:
		return [sorted(prefix)]
	elif n > len(l):
		return subset_n(l, n-1, prefix)
	elif n == len(l):
		return subset_n(l[1:], n-1, prefix + [l[0]])
	else:
		return subset_n(l[1:], n - 1, prefix + [l[0]]) + subset_n(l[1:], n, prefix)

def next_subset(n, nc, p, q, mtc):
	if not mtc:
		nc = 1
		q = [1]*(n+1)
		p = [0]*(n+1)
		p[1] = n
		return nc, p, q, nc != n
	else:
		m = n
		l = q[m]
		while p[l] == 1:
			q[m] = 1
			m = m - 1
			l = q[m]
		nc = nc + m - n
		p[1] = p[1] + n - m
		if l == nc:
			nc += 1
			p[nc] = 0
		q[m] = l+1
		p[l] = p[l] - 1
		p[l+1] = p[l+1] + 1
		return nc, p, q, nc != n

