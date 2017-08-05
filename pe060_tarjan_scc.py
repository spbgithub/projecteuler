index     = 0
g_index   = {}
g_lowlink = {}
g_onstack = {}
s         = []
scc       = []

def tarjan_scc(graph):
	for p in graph:
		g_index[p]   = -1
		g_lowlink[p] = -1
		g_onstack[p] = -1

	for p in graph:
		if g_index[p] == -1:
			strongconnect(p)


def strongconnect(v, graph):
	g_index[v]   = index
	g_lowlink[v] = index
	index        = index + 1
	s.append(v)
	g_onstack[v] = True

	for w in graph[v]:
		if g_index[w] == -1:
			strongconnect(w, graph)
			g_lowlink[v] = min(g_lowlink[v], g_lowlink[w])
		elif g_onstack[w]:
			g_lowlink[v] = min(g_lowlink[v], g_index[w])

	if g_lowlink[v] == g_index[v]:
		new_scc = []
		w = s.pop()
		while w != v:
			new_scc.append(w)
			g_onstack[w] = False
			w = s.pop()
		scc.append(new_scc)


